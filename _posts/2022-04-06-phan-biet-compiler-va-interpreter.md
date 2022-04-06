---
layout: post
title: "Phân biệt Compiler và Interpreter"
author: [rylie, htung]
categories: [computer science]
tags: [coding]
image: assets/images/posts/04-06-2022-phan-biet-compiler-interpreter/banner.png
description: "Khi bắt đầu học lập trình, bạn sẽ nhiều lần bắt gặp khái niệm về Compiler và Interpreter. Chúng đều là những translator, có nhiệm vụ dịch mã nguồn thành các chỉ dẫn mà máy tính có thể hiểu và thực hiện (machine code). Nắm bắt được sự khác nhau cơ bản giữa hai khái niệm này sẽ giúp các bạn phân biệt mục đích của các ngôn ngữ lập trình và cách thức xử lý chúng."
featured: true
---
Khi bắt đầu học lập trình, bạn sẽ nhiều lần bắt gặp khái niệm về Compiler và Interpreter. Chúng đều là những translator, có nhiệm vụ dịch mã nguồn thành các chỉ dẫn mà máy tính có thể hiểu và thực hiện (machine code). Nắm bắt được sự khác nhau cơ bản giữa hai khái niệm này sẽ giúp các bạn phân biệt mục đích của các ngôn ngữ lập trình và cách thức xử lý chúng.

## So sánh tổng quát

|  | Compiler | Interpreter |
| --- | --- | --- |
| Cách hoạt động | Dịch toàn bộ mã nguồn sang mã máy rồi cho ra một file thực thi. | Dịch từng đoạn mã nguồn sang mã máy và chạy trực tiếp. |
| Khi nào quá trình được chạy | Quá trình xảy ra khi mã nguồn được compiled cho ra file thực thi. Từ đó chỉ cần chạy file thực thi. | Quá trình xảy ra mỗi lần mã nguồn được chạy. |
| Xử lý lỗi | Compiler sẽ hiển thị các lỗi tìm được sau khi rà quét toàn bộ mã nguồn.<br />File thực thi sẽ không được cho ra. | Interpreter hiển thị lỗi ngay khi gặp phải một statement có chứa lỗi, đồng thời dừng chạy chương trình ngay lập tức. |
| Hiệu năng | Tốc độ chạy nhanh. | Tốc độ chạy chậm. |
| Môi trường chạy | Có thể chạy trực tiếp trên các máy tương thích. | Các máy phải tải môi trường phù hợp để chạy như Python. |
| Các ngôn ngữ tiêu biểu | C, C++, Rust | Python, PHP, Ruby, JavaScript |

## Cách thức hoạt động

### Compiler

Compiler tổng hợp và sắp xếp các dòng trong mã nguồn và dịch chúng về ngôn ngữ máy. Các library được sử dụng cũng sẽ được tập hợp lại và dùng trong quá trình compile. Cuối cùng, compiler sẽ trả lại mội  một file thực thi (chẳng hạn như file **.exe** trên Windows hay **.out** trên Mac, Linux) mà bạn có thể chạy được.

### Interpreter

Hiểu đơn giản, các interpreted languages sẽ xử lý thẳng file mã nguồn, thay vì trải qua nhiều bước để có được file thực thi (ví dụ như file .exe) như các compiled languages.

Interpreted languages thường sử dụng một trong 3 cách hoạt động sau:

1. Phân tích cú pháp của từng dòng mã nguồn và thực thi chúng.
2. Dịch mã nguồn sang một **intermediate language** (ngôn ngữ trung cấp) và thực thi chúng.
3. Compile native code cho **virtual machine** (máy ảo) của ngôn ngữ đó và chạy trên máy ảo.

## Khi nào quá trình compile/interpret bắt đầu

### Compiler

Quá trình compile mã nguồn sẽ diễn ra khi có sự thay đổi trong mã nguồn. Ngoài ra, ta chỉ cần chạy file thực thi và không cần compile lại nữa.

### Interpreter

Trái với việc chỉ cần compile mã nguồn một lần rồi chạy, quá trình interpret mã nguồn luôn xảy ra mỗi khi ta chạy file mã nguồn kể cả khi nó không thay đổi, bởi vì interpreter không tạo ra file thực thi.

## Hiệu năng

### Compiler

Một chương trình viết bằng một compiled language thường sẽ tốn không nhiều thời gian để khởi động. Compiler sau khi dịch xong mã nguồn thì sẽ cho ra một file thực thi, tức là không cần phải dịch lại mã nguồn mỗi lần chạy chương trình mà chỉ cần khởi động file thực thi. Compiler còn tối ưu hóa mã nguồn cho một hệ điều hành cụ thể để nó có thể chạy trơn tru trên hệ điều hành đó.

Lấy ví dụ về ngôn ngữ C++, khi ta khởi động một chương trình C++, ta sẽ chỉ cần compile mã nguồn một lần và chạy file thực thi (chẳng hạn như file .exe trên Windows) bao nhiêu lần cũng được.

### Interpreter

Một chương trình viết bằng một interpreted language thường sẽ mất nhiều thời gian để khởi động hơn so với một chương trình viết bằng một compiled language. Như đã đề cập ở trên, ta có một vài cách thức chủ yếu để một đoạn mã nguồn viết bằng interpreted language hoạt động trên máy tính, và quá trình dịch mã nguồn ra intermediate language hay khởi động máy ảo của ngôn ngữ đó *cho mỗi lần chạy* thường tốn nhiều thời gian hơn so với việc compile mã nguồn - có thể lâu nếu codebase lớn, nhưng sau đó không cần phải compile lại mà chỉ cần chạy trực tiếp.

Giả sử như đối với Java, nói một cách rất đơn giản, khi ta chạy một chương trình Java, có thể coi như có các bước sau:

1. Dịch mã nguồn ra ngôn ngữ trung cấp - được gọi là **Java bytecode.**
2. Khởi động máy ảo Java.
3. Đưa Java bytecode từ bước 1 vào máy ảo Java và thực thi code.

Tuy không cần compile mã nguồn trước khi chạy, nhưng những chương trình bằng Java sẽ phải trải qua tất cả các bước đó *mỗi lần chạy* mã nguồn, và việc đó tốn tương đối nhiều thời gian so với việc chạy thẳng mã nguồn được compile cho hệ máy ta đang dùng.

## Môi trường chạy

### Compiler

Khác so với các interpreted language, compiled language có khả năng dùng các file runtime có các library cần thiết để khởi động file thực thi sau khi compile.

Bạn không nhất thiết phải setup toàn bộ môi trường chạy gồm có compiler, debugger, v.v

### Interpreter

Trái với điều ở trên, các interpreted language thường yêu cầu người dùng cài đặt toàn bộ môi trường chạy của ngôn ngữ đó ở trên máy, và thường thì nó sẽ cồng kềnh hơn so với việc cài đặt các file runtime của các compiled languages.

Ví dụ như Java sẽ yêu cầu người dùng cài đặt một phiên bản Java, trong đó gồm có Java Virtual Machine, Python thì cần có interpreter Python, tương tự đối với Ruby, v.v.

Việc setup Python ở trên máy tính sẽ tốn khoảng 115 MB, chưa tính các library khác mà người dùng sẽ phải cài nếu mã nguồn yêu cầu, còn việc cài đặt bộ runtime Visual C++ 2015-2019 chỉ tốn khoảng 50 MB, mà điều này cũng chưa hẳn là cần thiết nếu mã nguồn không sử dụng đến các library này.

## Một số ngôn ngữ điển hình

### Compiled

- C++
- C
- Pascal
- Objective-C
- Rust

Lưu ý rằng những compiled languages không nhất thiết phải cho vào compiler. Đã có những nỗ lực phát triển những compiler các ngôn ngữ này. Một ví dụ điển hình là Cling của C++.

### Interpreted

- Python
- Ruby
- Java
    - Java là một trường hợp tương đối đặc biệt, vì khi nhìn nó theo những tiêu chí được đề ra khi thiết kế ngôn ngữ, nó được gọi là một interpreted language.
    - Tuy nhiên, cách thức hoạt động của Java lại gần như sự kết hợp của cả hai - mã nguồn được dịch ra một ngôn ngữ trung cấp là Java bytecode, nhưng trong quá trình thực thi có thể sử dụng tới **Just-In-Time Compiler**, phần nào đó dịch một số đoạn mã nguồn ra native code dành cho hệ máy đó để có thể tăng tốc độ xử lý.

## Kết luận

Tóm lại, compiler và interpreter đều hoạt động khác biệt với nhau, đi kèm đó là những ưu điểm và nhược điểm riêng của mỗi loại. Tùy vào mục đích sử dụng mà bạn có thể cân nhắc giữa compiled và interpreted language. Nếu chú trọng hiệu năng ứng dụng thì Compiling là một lựa chọn sáng giá, còn nếu muốn phát triển ứng dụng nhanh thì Interpreting sẽ phù hợp hơn.