---
layout: post
title: "[CODE MUSIC BOT FOR DISCORD] - Phần 1: Cài đặt môi trường"
author: [khiem]
categories: [javascript]
tags: [coding]
image: assets/images/posts/2022-04-29-discord-music-bot-1/banner.jpg
description: "Đầu tiên, UCC xin chân thành cảm ơn các bạn đã quan tâm và tham gia buổi Seminar tạo Discord Music Bot vừa qua. Có lẽ sẽ có nhiều bạn chưa thể tham gia hay vẫn còn cảm thấy chưa rõ về buổi Seminar đó. Hôm nay, UCC sẽ có một series blog về cách hướng dẫn tạo một con bot có thể chơi nhạc trên Discord vô cùng chi tiết. Ở bài blog đầu tiên này mình sẽ hướng dẫn các bạn cách cài đặt môi trường* để con bot Discord có thể chạy trên máy tính của bạn. À, nếu có gì vẫn còn băn khoăn thì bạn có thể inbox trực tiếp fanpage của UCC để hỏi, chúng mình luôn sẵn sàng giải đáp các thắc mắc của bạn."
featured: false
---

Đầu tiên, **UCC** xin chân thành cảm ơn các bạn đã quan tâm và tham gia buổi Seminar tạo **Discord Music Bot** vừa qua. Có lẽ sẽ có nhiều bạn chưa thể tham gia hay vẫn còn cảm thấy chưa rõ về buổi Seminar đó. Hôm nay, **UCC** sẽ có một **series blog** về cách hướng dẫn tạo một con bot có thể chơi nhạc trên **Discord** vô cùng chi tiết. Ở bài blog đầu tiên này mình sẽ hướng dẫn các bạn cách **cài đặt môi trường** để con **bot Discord** có thể chạy trên máy tính của bạn. À, nếu có gì vẫn còn băn khoăn thì bạn có thể **inbox** trực tiếp [fanpage của UCC](https://www.facebook.com/USTH.Coders.Club) để hỏi, chúng mình luôn **sẵn sàng giải đáp** các thắc mắc của bạn.

## Cài đặt Node.js

Vì ngôn ngữ mình sử dụng là **JavaScript**, nên trước khi code bot mình sẽ tiến hành cài **Node.js**. **Node.js** là một môi trường độc lập giúp bạn có thể thực hiện chạy code **JavaScript** bên ngoài trình duyệt. Để cài đặt **Node.js** bạn truy cập website [nodejs.org](http://nodejs.org) và chọn bản **LTS** (**long-term support**) bởi đây là phiên bản **ổn định nhất**.

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/nodejsdownload.png" alt="nodejsdownload.png"></p>

Sau khi đã tải về, bạn mở nó lên và tiến hành cài đặt như từng bước như hình:

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install1.png" alt="install1.png"></p>

> Các bạn bấm **Next** để tiếp tục
> 

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install2.png" alt="install2.png"></p>

> Tích vào ô chấp nhận điều khoản rồi tiếp tục bấm **Next**
> 

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install3.png" alt="install3.png"></p>

> Chọn vị trí nơi bạn muốn lưu rồi tiếp tục bấm **Next**
> 

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install4.png" alt="install4.png"></p>

> Đoạn này bạn tiếp tục bấm **Next**
> 

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install5.png" alt="install5.png"></p>

> Bạn có thể tích vào ô trên để cài đặt một số công cụ khác (*Optional*). Rồi bạn bấm **Next** để tiếp tục.
> 

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install6.png" alt="install6.png"></p>

> Bấm **Install** để bắt đầu cài đặt
> 

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install7.png" alt="install7.png"></p>

> Bạn đợi một lúc để chương trình cài đặt.
> 

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install8.png" alt="install8.png"></p>

> Bấm **Finish** để hoàn tất cài đặt.
> 

Để kiểm tra xem đã cài đặt thành công chưa, bạn mở **PowerShell** và nhập **`node -v`** để kiểm tra phiên bản **Nodejs**. Nếu nó hiện đúng phiên bản thì bạn đã cài đặt thành công.

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/install_success.png" alt="install_success.png"></p>

## Cài đặt các module cần thiết

Sau khi đã cài thành công Nodejs, tiếp theo chúng ta sẽ đến phần cài đặt các module cần thiết để code con bot. Giống như C hay Python chúng ta được học ở trường cần phải khai báo một số thư viện như **stdio.h**, **math.h** hoặc **pygame**, con bot của chúng ta cũng yêu cầu một số **module** để có thể hoạt động được. Trước tiên bạn hãy tạo một folder để chứa các file code (**Lưu ý**: tên folder không được để có dấu). 

Ví dụ mình tạo một folder tên **DiscordBot** như trong ảnh:

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/mkdir.png" alt="mkdir.png"></p>

Để mở **PowerShell** tại đúng folder mình code, bạn chỉ cần nhập “**powershell**” tại ô địa chỉ folder:

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/open_pws.png" alt="open_pws.png"></p>

Tiếp theo chúng ta sẽ tiến hành cài các modules. Đầu tiên nhập lệnh **`npm init`** để tạo file package.json (đây là file chứa thông tin và các module của bạn). Bạn chỉ cần bấm **Enter** đến khi hiện giống trong hình dưới đây là ok:

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/npm_init.png" alt="npm_init.png"></p>

Tiếp đến bạn hãy nhập:

`npm install discord.js discord-player dotenv ffmpeg-static @discordjs/opus`

<p style="text-align: center;"><img src="/assets/images/posts/2022-04-29-discord-music-bot-1/npm_install.png" alt="npm_install.png"></p>

Câu lệnh trên sẽ tự động cài các modules:

- **discord.js**: cho phép bạn tương tác với Discord qua JavaScript
- **discord-player**: một framework hoàn chỉnh để đơn giản hóa lệnh phát nhạc qua discord.js
- **dotenv**: lấy dữ liệu trong file môi trường **.env**
- **ffmpeg-static**: xử lý âm thanh
- **@discordjs/opus**: cũng là xử lý âm thanh luôn

Vậy là chúng ta đã hoàn thành xong những bước đầu tiên bao gồm cài đặt môi trường cần thiết để một con bot Discord hoạt động. Ở bài viết tiếp theo, UCC sẽ hướng dẫn các bạn cách tạo ra con bot và làm nó chạy được bằng code. Và cuối cùng, nếu gặp lỗi hay khó khăn gì thì đừng ngần ngại, hãy inbox trực tiếp [fanpage UCC](https://www.facebook.com/USTH.Coders.Club) nhé!