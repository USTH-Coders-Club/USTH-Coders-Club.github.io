---
layout: post
title: "Phân tích lỗ hổng OS Command Injection trong ứng dụng SolarView Compact 6.0"
author: [nhatthanh]
categories: [security]
tags: [code, security]
image: assets\images\posts\2022-07-19-solar-view\banner.png
description: "Hôm nay UCC sẽ đổi gió bằng một bài viết về chủ đề Security. Hãy cùng chúng mình tìm hiểu về một trong những lỗ hổng ứng dụng web cơ bản nhất - OS Command Injection - bằng cách phân tích một ví dụ thực tế từ một máy chủ đặt tại Nhật Bản. Các nhà nghiên cứu bảo mật đã tìm ra lỗ hổng OS Command Injection trong chức năng kiểm tra email của ứng dụng SolarView Compact phiên bản **6.0**. Lỗ hổng này đã được chương trình CVE của tập đoàn MITRE công nhận và gán cho mã định danh CVE-2022-29303 với điểm số mức độ nghiêm trọng là 9.8 CRITICAL, cho phép kẻ tấn công có thể chiếm quyền hệ thống."
featured: true  
toc: true
---

Hôm nay UCC sẽ đổi gió bằng một bài viết về chủ đề Security. Hãy cùng chúng mình tìm hiểu về một trong những lỗ hổng ứng dụng web cơ bản nhất - **OS Command Injection** - bằng cách phân tích một ví dụ thực tế từ một máy chủ đặt tại Nhật Bản. Các nhà nghiên cứu bảo mật đã tìm ra lỗ hổng OS Command Injection trong chức năng kiểm tra email của ứng dụng SolarView Compact phiên bản **6.0**. Lỗ hổng này đã được chương trình [CVE](https://www.redhat.com/en/topics/security/what-is-cve) của tập đoàn MITRE công nhận và gán cho mã định danh **CVE-2022-29303** với điểm số mức độ nghiêm trọng là **9.8 CRITICAL**, cho phép kẻ tấn công có thể chiếm quyền hệ thống.  

## Giới thiệu về SolarView

**SolarView Compact** là một ứng dụng web được viết bằng PHP, có nhiệm vụ theo dõi [hệ thống năng lượng mặt trời](https://www.contec.com/solutions/energy/solutions/solar-battery/) dành cho doanh nghiệp và trường học do công ty Nhật Bản **CONTEC** cung cấp. Mô hình chung của hệ thống được biểu diễn như hình minh họa dưới đây:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled.png" alt="Untitled.png"></p>


Toàn bộ dữ liệu từ các thiết bị như tấm pin năng lượng mặt trời, cảm biến, … sẽ được thu thập bởi thiết bị SolarView Compact (cụ thể là mã sản phẩm [SV-CPT-MC310](https://www.contec.com/products-services/environmental-monitoring/solarview/pv-package/sv-cpt-mc310/feature/#section)) sau đó hiển thị qua một ứng dụng chạy trên web server giúp truy cập từ xa:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 1.png" alt="Untitled.png"></p>


Sản phẩm SV-CPT-MC310 trên trang chủ CONTEC

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 2.png" alt="Untitled.png"></p>


Giao diện của ứng dụng web SolarView Compact

## Phân tích lỗ hổng trong mã nguồn SolarView Compact 6.0

### Code Logic

Bằng những “biện pháp nghiệp vụ”, UCC đã tìm ra địa chỉ IP của một máy chủ Nhật Bản đang chạy phiên bản dính lỗ hổng của ứng dụng SolarView Compact.

Lỗ hổng OS Command Injection tồn tại trong chức năng kiểm tra email của ứng dụng web có tên là **conf_mail.php** (giao diện này đã được Google Translate tự động dịch sang Tiếng Anh, ở phiên bản gốc, toàn bộ chữ trên giao diện là Tiếng Nhật):

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 3.png" alt="Untitled.png"></p>


Theo như giao diện, chúng ta có thể đoán được chức năng của conf_mail.php là gửi một email kiểm tra đến địa chỉ mail mà người dùng nhập vào:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 4.png" alt="Untitled.png"></p>

Sử dụng phần mềm **BurpSuite**, chúng ta có thể quan sát được request được trình duyệt gửi đi sau khi bấm nút “send e-mail”:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 5.png" alt="Untitled.png"></p>

Khi bấm nút “send e-mail”, trình duyệt sẽ gửi một **POST** request lên **conf_mail.php**, và địa chỉ email người dùng nhập vào sẽ được đặt bên trong parameter “**mail_address**”. Còn parameter **button** chỉ là tên của cái nút đó (”send e-mail” trong tiếng Nhật). Toàn bộ phần body đã được mã hóa URL encode. 

Tiếp theo chúng ta sẽ kiểm tra mã nguồn của file **conf_mail.php**:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 6.png" alt="Untitled.png"></p>


Dòng 2, 3, 4, server đang khởi tạo giá trị của 2 biến **$button** và **$mail_address** dựa theo giá trị của 2 parameter tương ứng trong phần body của **POST** request mà chúng ta đã quan sát được ở phía trên:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 7.png" alt="Untitled.png"></p>


Vậy là khi server nhận được **POST** request, biến **$button** sẽ nhận giá trị là chữ tiếng Nhật, dịch ra  “send e-mail”, còn biến **$mail_address** nhận giá trị là “admin@admin.com”. Dòng 6, 7, 8, 9 server đang import một số biến và hàm từ bên ngoài:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 8.png" alt="Untitled.png"></p>


Dòng 12 server kiểm tra lại tên của biến $button xem có tương đương với nội dung biến **$LABEL_SENDEXEC** hay không (biến này có thể server đã import từ dòng 6, 7, 8, 9):

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 9.png" alt="Untitled.png"></p>


Dòng 13, server cố gắng loại bỏ toàn bộ dấu cách trong biến **$mail_address**:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 10.png" alt="Untitled.png"></p>


Tiếp theo là đoạn code thú vị nhất:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 11.png" alt="Untitled.png"></p>


Dòng 14 kiểm tra biến $mail_address có đủ độ dài trên 3 hay không. Tiến vào đoạn code bên trong hàm if, chúng ta thấy server khởi tạo một biến mới tên là **$sendmes** có nội dung là một đoạn tiếng Nhật nào đó: 

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 12.png" alt="Untitled.png"></p>


**Conf_mail.php** tiếp tục khởi tạo biến **$exec_cmd** có nội dung là một câu lệnh Linux có chức năng thêm 1 dòng chữ vào file **/dev/elogparam** nằm trong server:

```php
$exec_cmd = "echo -1 ".$mail_address." TEST-MAIL '$sendmes' > /dev/elogparam";
```

Nội dung biến **$mail_address** và **$sendmes** được ghép vào tạo thành một câu lệnh hoàn chỉnh lưu trong biến **$exec_cmd**. Vậy với **mail_address** chúng ta ban đầu nhập là admin@admin.com, biến **$exec_cmd** sẽ có nội dung như sau:

```bash
echo -1 admin@admin.com TEST-MAIL 本メールはSolarViewが送信したテストメールです。> /dev/elogparam
```

Sau đó, **conf_mail.php** thực thi câu lệnh này bằng cách đưa nội dung biến **$exec_cmd** vào hàm **system()**:

```php
system( $exec_cmd );
```

### Khai thác lỗ hổng

Vậy chính xác lỗ hổng OS Command Injection nằm ở đâu? Câu trả lời chính là ở dòng 16, khi server ghép nội dung biến **$mail_address** vào câu lệnh **$exec_cmd**. Do mã nguồn không hề có bước thanh lọc user input, kẻ tấn công thay vì nhập một email hợp lệ như thông thường, họ sẽ chèn thêm câu lệnh Linux.

Thay vì nhập:

```php
admin@admin.com
```

Hách cơ sẽ nhập:

```bash
;id;
```

“id” trong Linux là một câu lệnh hiển thị thông tin user hiện tại. Khi nhập payload trên, tại dòng 16, biến **$exec_cmd** sẽ có giá trị như sau:

```bash
echo -1 ;id; TEST-MAIL '$sendmes' > /dev/elogparam
```

Như vậy, khi biến này được đưa vào hàm system(), thực tế sẽ có 3 lệnh được thực thi:

- echo -1: in ra “-1”
- **id**: hiển thị thông tin user
- TEST-MAIL '$sendmes' > /dev/elogparam: chạy một binary có tên “TEST-MAIL” và đưa output vào file /dev/elogparam, nhưng vì binary này không tồn tại nên câu lệnh này sẽ bị lỗi

Chúng ta có thể thấy, kẻ tấn công đã thành công trong việc thực thi lệnh bất kỳ trên hệ thống bằng cách sử dụng dấu ; để cô lập câu lệnh mới với 2 phần trước và sau biến $exec_cmd gốc. Thay vì “id”, kẻ tấn công có thể thực hiện bất kỳ câu lệnh nào họ muốn, đồng nghĩa họ đã kiểm soát được server.

Hãy cùng kiểm chứng với mục tiêu UCC đã tìm thấy. Sử dụng phần mềm Burp Suite để thay đổi nội dung request đến server:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 13.png" alt="Untitled.png"></p>


Tại parameter mail_address, chúng ta thay đổi email thông thường thành “**;id**;” (dấu ; khi được mã hóa url sẽ trở thành **%3B**). Gửi request này lên server và chúng ta nhận được response:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 14.png" alt="Untitled.png"></p>


Output của câu lệnh đã được trả về thành công. Vậy còn những câu lệnh yêu cầu param thì sao? Server đã có một dòng code loại bỏ toàn bộ dấu cách. Làm như thế nào để chèn được câu lệnh hợp lệ chứa dấu cách?

Để bypass dòng code này, chúng ta sẽ sử dụng biến môi trường có sẵn trên Linux đó là **IFS**, viết tắt của Internal Field Separator (nói trắng ra là dấu cách). Như vậy, để thực thi một câu lệnh như `cat /etc/passwd` trên server, chúng ta sẽ chèn `;cat${IFS}/etc/passwd;` dưới dạng mã hóa URL (tuân thủ header Content-Type: application/x-www-form-urlencoded)

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 15.png" alt="Untitled.png"></p>


Và nhận được response:

<p style="text-align: center;"><img src="/assets/images/posts/2022-07-19-solar-view/Untitled 16.png" alt="Untitled.png"></p>

Các bạn hãy theo dõi UCC để đón đọc những bài viết về chủ đề Security tiếp theo nhé!
