---
layout: post
title: "Phân biệt Compiler và Interpreter"
author: [rylie, htung]
categories: [computer science]
tags: [coding]
image: assets/images/posts/04-06-2022-phan-biet-compiler-interpreter/banner.png
description: "Khi bắt đầu học lập trình, bạn sẽ nhiều lần bắt gặp khái niệm về Compiler và Interpreter. Chúng đều là những translator, có nhiệm vụ dịch mã nguồn thành các chỉ dẫn mà máy tính có thể hiểu và thực hiện (machine code). Nắm bắt được sự khác nhau cơ bản giữa hai khái niệm này sẽ giúp các bạn phân biệt mục đích của các ngôn ngữ lập trình và cách thức xử lý chúng."
featured: false
toc: true
---
Khi bắt đầu học lập trình, bạn sẽ nhiều lần bắt gặp khái niệm về Compiler và Interpreter. Chúng đều là những translator, có nhiệm vụ dịch mã nguồn thành các chỉ dẫn mà máy tính có thể hiểu và thực hiện (machine code). Nắm bắt được sự khác nhau cơ bản giữa hai khái niệm này sẽ giúp các bạn phân biệt mục đích của các ngôn ngữ lập trình và cách thức xử lý chúng.


## So sánh tổng quát

|  | Compiler | Interpreter |
| --- | --- | --- |
| Cách hoạt động | Dịch toàn bộ mã nguồn sang mã máy rồi cho ra một file thực thi. | Dịch từng đoạn mã nguồn sang mã máy và chạy trực tiếp. |
| Hiệu năng | Thường có hiệu năng cao hơn. | Thường có hiệu năng thấp hơn |
| Môi trường chạy | Có thể chạy trực tiếp trên các máy tương thích. | Các máy phải tải môi trường phù hợp để chạy như Python. |
| Các ngôn ngữ tiêu biểu | C, C++, Rust | Python, PHP, Ruby |

## 1. Cách thức hoạt động

### Compiler

Compiler tổng hợp và sắp xếp các dòng trong mã nguồn và dịch chúng về ngôn ngữ máy. Các library được sử dụng cũng sẽ được tập hợp lại và dùng trong quá trình compile. Cuối cùng, compiler sẽ trả lại file thực thi (chẳng hạn như file **.exe** trên Windows) mà bạn có thể chạy được. Việc này đồng nghĩa nếu mã nguồn không bị thay đổi thì bạn có thể chạy file thực thi đó mà không phải compile lại mỗi lần chạy.

### Interpreter

Interpreter sẽ dịch từng đoạn mã nguồn sang mã máy và chạy chúng luôn thay vì tổng hợp hết lại về một file thực thi. Ngoài ra một số biến thể khác của interpreter có thể hoạt đông theo cách dịch mã nguồn về native code cho **virtual machine** (máy ảo) của ngôn ngữ đó và chạy trên máy ảo. VD: Java. Thường quá trình interpret sẽ luôn chạy khi bạn chạy code dù cho mã nguồn không có sự thay đổi.

## 2. Hiệu năng

### Compiler

Như đã đề cập ở trên, compiler chỉ cần dịch mã nguồn một lần và tạo ra file thực thi; chính vì vậy, ứng dụng của bạn sẽ được tối ưu hóa và chạy nhanh hơn.

### Interpreter

Các ứng dụng được viết bằng interpreted language thường sẽ dịch lại mã nguồn mỗi lần chạy hoặc phải khởi động máy ảo vì vậy sẽ tốn thời gian hơn.

### Ví dụ:

Hãy tưởng tượng bạn có 2 ứng dụng có tính năng giống nhau; nhưng ứng dụng A được viết bằng compiled language và ứng dụng B được viết bằng interpreted language. Nếu bạn chạy 2 ứng dụng đó 5 lần thì ứng dụng A chỉ cần compile một lần. Trái lại ứng dụng B phải được interpret 5 lần. Vì thế mà ứng dụng A mỗi lần chạy sẽ nhanh hơn ứng dụng B.

Tuy nhiên xét về việc bạn muốn thêm tính năng hay thay đổi mã nguồn của 2 ứng dụng này. Cả 2 ứng dụng đều phải compile và interpret lại mỗi khi bạn thay đổi mã nguồn. Nhưng quá trình compile thường sẽ chậm hơn interpret; vì vậy ứng dụng B lại được chạy nhanh hơn ứng dụng A. 

## 3. Môi trường chạy

### Compiler

Do đã được compile về file thực thi, compile language có thể chạy trên máy tính mà không cần có môi trường đặc biệt.

### Interpreter

Interpreted language thường yêu cầu người dùng cài đặt môi trường chạy của ngôn ngữ đó ở trên máy. Ví dụ như Java sẽ yêu cầu người dùng cài đặt một phiên bản Java, trong đó gồm có Java Virtual Machine, Python thì cần có interpreter Python, tương tự đối với Ruby, ...

## 4. Một số ngôn ngữ điển hình

### Compiled

- C++
- C
- Pascal
- Objective-C
- Rust

### Interpreted

- Python
- Ruby
- PHP

### Ngoại lệ

- Java: cách thức hoạt động của Java lại gần như sự kết hợp của cả hai - mã nguồn được dịch ra một ngôn ngữ trung cấp là Java bytecode, nhưng trong quá trình thực thi có thể sử dụng tới **Just-In-Time Compiler**, phần nào đó dịch một số đoạn mã nguồn ra native code dành cho hệ máy đó để có thể tăng tốc độ xử lý.

## Kết luận

Tóm lại, compiler và interpreter đều hoạt động khác biệt với nhau, đi kèm đó là những ưu điểm và nhược điểm riêng của mỗi loại. Tùy vào mục đích sử dụng mà bạn có thể cân nhắc giữa compiled và interpreted language. Nếu chú trọng hiệu năng ứng dụng thì Compiled Languages là lựa chọn sáng giá; còn nếu muốn đẩy nhanh phát triển ứng dụng thì Interpreted Languages có thể sẽ tối ưu hơn.
