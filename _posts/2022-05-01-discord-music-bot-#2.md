---
layout: post
title: "[CODE MUSIC BOT FOR DISCORD] - Phần 2: Một số lệnh cơ bản"
author: [nhatthanh]
categories: [javascript]
tags: [coding]
image: assets/images/posts/2022-05-01-discord-music-bot-2/banner.jpg
description: "Ở Phần 1, UCC đã hướng dẫn các bạn cài đặt môi trường cho con bot hoạt động bao gồm Node.js và một số module đi kèm. Trong bài này, chúng mình sẽ chỉ cho bạn cách thiết lập một tài khoản Bot trong Discord, sau đó đăng nhập nó và code một số lệnh cơ bản bằng Javascript. Oke gét gô!"
featured: false
---

Ở Phần 1, **UCC** đã hướng dẫn các bạn cài đặt môi trường cho con bot hoạt động bao gồm **Node.js** và một số module đi kèm. Trong bài này, chúng mình sẽ chỉ cho bạn cách thiết lập một tài khoản Bot trong Discord, sau đó đăng nhập nó và code một số lệnh cơ bản bằng **Javascript**. Oke gét gô!

## Thiết lập tài khoản cho Bot

### 1. Đăng ký với Discord

Để có một con Bot và điều khiển nó bằng code, đầu tiên chúng ta cần phải đăng ký với Discord. Các bạn hãy truy cập [https://discord.com/developers/appilcation](https://discord.com/developers/applications):

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled.png" alt="Untitled.png"></p>


Sau đó hãy bấm nút “**New Application**”, sau đó đặt cho App một cái tên (**Lưu ý**: Tên này chưa phải là tên Bot nha!):

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 1.png" alt="Untitled 1.png"></p>

Bấm “**Create**” và giao diện dưới đây sẽ hiện ra. Các bạn hãy bấm nút “**Bot**” ở phía bên trái:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 2.png" alt="Untitled 2.png"></p>

Sau đó bạn bấm “**Add Bot**” để tạo tài khoản bot:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 3.png" alt="Untitled 3.png"></p>

Discord sẽ cho bạn một tài khoản bot. Tại đây bạn có thể đổi tên cho con bot tùy thích ở ô “**USERNAME**” nha! Sau đó nhớ bấm “**Save changes**” để lưu:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 4.png" alt="Untitled 4.png"></p>

Tiếp theo, chúng ta cần phải cấp cho Bot một số quyền để nó có thể hoạt động mượt mà. Cuộn xuống một chút bạn sẽ thấy mục “**Privileged Gateway Intents**”, sau đó hãy click vào hai nút này:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 5.png" alt="Untitled 5.png"></p>

Hai nút đó sẽ cho con Bot của chúng ta có quyền lấy **danh sách thành viên** trong server và **đọc các tin nhắn** được gửi trong server đó.

### 2. Thêm Bot vào Server

Trước tiên để thêm một con bot vào server, bạn cần tạo một server Discord trước đã. Nếu bạn đã có server rồi thì hãy chắc chắn mình có quyền quản lý server đó, nếu không thì bạn sẽ không thể thêm con Bot vào. Để tạo một server mới, hãy truy cập đến [https://discord.com/app](https://discord.com/channels/@me), sau đó tìm đến nút **+** ở phía bên trái:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 6.png" alt="Untitled 6.png"></p>

Nhấp “**Create My Own**”:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 7.png" alt="Untitled 7.png"></p>

Nhấp “**For me and my friends**”:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 8.png" alt="Untitled 8.png"></p>

Tại đây bạn có thể đặt tên và chọn avatar cho server của mình:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 9.png" alt="Untitled 9.png"></p>

Bấm “**Create**” là bạn đã có server của riêng mình rồi:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 10.png" alt="Untitled 10.png"></p>

Bây giờ bạn hãy quay lại với trang [Applications](https://discord.com/developers/applications), và chọn App vừa tạo lúc trước:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 11.png" alt="Untitled 11.png"></p>

Chọn “**OAuth2**” và “**URL Generator**”:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 12.png" alt="Untitled 12.png"></p>

Tại đây chúng ta sẽ tạo một đường link để mời Bot vào server. Để làm được việc này, các bạn hãy nhấp ô “**Bot**” và “**Administrator**”:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 13.png" alt="Untitled 13.png"></p>

Cuộn xuống cuối, bạn sẽ thấy một đường dẫn. Hãy copy đường dẫn này và mở trong một tab mới:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 14.png" alt="Untitled 14.png"></p>

Tại đây bạn có thể chọn server muốn thêm Bot vào, sau đó bấm “**Continue**”:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 15.png" alt="Untitled 15.png"></p>

Hooray vậy là con Bot của chúng ta đã ở trong server rồi:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 16.png" alt="Untitled 16.png"></p>

## Code các lệnh cơ bản bằng Javascript

Oke vậy là khâu chuẩn bị đã xong. Các bạn hãy bật **Visual Studio Code** lên và bắt đầu lập trình thôi. Đầu tiên hãy cài 2 extension là “**Code Runner**” và “**Javascript**” nha:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 17.png" alt="Untitled 17.png"></p>

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 18.png" alt="Untitled 18.png"></p>

### 1. Đăng nhập vào Bot

Ở trong **Visual Studio Code**, các bạn hãy mở thư mục đã tạo từ Phần 1 nhé. Nhấp vào **File →Open Folder** và chọn thư mục của bạn:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 19.png" alt="Untitled 19.png"></p>


Ở phần 1 chúng ta đã sử dụng lệnh **`npm init`** để tạo file **package.json** quản lý các module. Bây giờ các bạn tạo một file mới tên **.env** nha (**Lưu ý** dấu chấm là bắt buộc đó):

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 20.png" alt="Untitled 20.png"></p>


Ở file này, các bạn hãy thêm một dòng “**DISCORD_TOKEN=**” như dưới đây:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 21.png" alt="Untitled 21.png"></p>


Đến đây, các bạn hãy quay lại trang đăng ký Bot của mình và tìm đến nút “**Reset Token**” trong mục “**Bot**”:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 22.png" alt="Untitled 22.png"></p>

Nhấp vào đây và một dòng chữ loằng ngoằng sẽ hiện ra:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 23.png" alt="Untitled 23.png"></p>

Chính cái dòng loằng ngoằng này lại là một chiếc chìa khóa quan trọng giúp bạn đăng nhập được vào con Bot đã tạo và điều khiển nó. Chính vì vậy, bất kỳ ai sở hữu dòng chữ này sẽ có thể điều khiển được con Bot của bạn. Vậy nên **đừng** chia sẻ nó cho ai nhé! (Tẹo nữa mình cũng đổi Token đây). Bấm Copy và Paste nó vào file **.env** của chúng mình nhé:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 24.png" alt="Untitled 24.png"></p>

Okay, bắt tay vào code thôi! Giờ các bạn hãy tạo một file mới có tên **index.js**:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 25.png" alt="Untitled 25.png"></p>

Chúng ta sẽ cần đến Token ở file **.env** lúc nãy. Để nạp được file này, ta sẽ sử dụng module **dotenv**. Khai báo module này cũng đơn giản thôi:

```jsx
require('dotenv').config();
```

Tiếp theo, chúng ta cần nạp hai object là **Client** và **Intents** trong module **discord.js**. **Client** sẽ đảm nhiệm nhiệm vụ tương tác với Discord API, **Intents** sẽ cấp quyền cần thiết cho **Client**:

```jsx
const {
    Client,
    Intents,
} = require('discord.js');
```

Chúng ta sẽ nạp object **Player** trong module **discord-player**. **Player** sẽ đảm nhiệm nhiệm vụ xử lý các tác vụ về nhạc:

```jsx
const { Player } = require('discord-player');
```

Chúng ta sẽ tạo một “**Client**” mới để sử dụng và cấu hình nó với một số quyền:

```jsx
const client = new Client({ intents: [
    Intents.FLAGS.GUILDS,
    Intents.FLAGS.GUILD_MESSAGES,
    Intents.FLAGS.GUILD_VOICE_STATES,
    "GUILD_MEMBERS",
] });
```

**client** (object điều khiển bot) mới tạo của chúng ta sẽ có quyền quản lý danh sách server mà nó được thêm vào, quyền đọc tin nhắn trong server, quyền lấy trạng thái kênh voice và quyền lấy danh sách thành viên trong server. Tiếp theo chúng ta cũng sẽ tạo một “**Player**” mới để sử dụng:

```jsx
const player = new Player(client);
```

Khi chúng ta sử dụng Discord, những hành động khác nhau sẽ kích hoạt các hàm khác nhau trong client. Ví dụ như khi chúng ta gửi tin nhắn, react tin nhắn, xóa tin nhắn, ... . Các hành động đó gọi là **event**, và con bot của chúng ta sẽ phản hồi lại những event đó theo cách mà chúng ta muốn. Ví dụ, khi con bot của chúng ta đã được login thành công bằng Token, nó sẽ kích hoạt một event gọi là “**ready**”. Dưới đây là đoạn code sẽ được chạy nếu event này được kích hoạt:

```jsx
client.on('ready', () => {
    console.log('minccino ready!');
});
```

Khi event “**ready**" được kích hoạt, đoạn code trong ngoặc nhọn của chúng ta sẽ được chạy, trong trường hợp này là in ra một dòng “**minccino ready!**”. Tiếp theo chúng ta hãy thử đăng nhập vào con bot nhé:

```jsx
client.login(process.env.DISCORD_TOKEN);
```

Đoạn **`process.env.DISCORD_TOKEN`** sẽ lấy biến **DISCORD_TOKEN** trong file **.env** của chúng ta. Xong rồi bấm chạy code thôi:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 26.png" alt="Untitled 26.png"></p>

Dòng “**minccino ready!**” đã được in ra đồng nghĩa con bot của bạn đã được login thành công. Vào trong server Discord bạn có thể thấy nó đang online:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 27.png" alt="Untitled 27.png"></p>

### 2. Xử lý tin nhắn đơn giản

Yay! Vậy là chúng ta đã đi được nửa con đường rồi! Con bot này mới chỉ Online thôi chứ vẫn chưa làm được gì cả, vì chúng ta chưa xử lý các event khác. Bây giờ ta sẽ thử làm cho con Bot nói “**Pong**” mỗi khi ta gửi tin nhắn “**Ping**” nhé! Mỗi khi người dùng trong server gửi một tin nhắn, event “**messageCreate**” sẽ được kích hoạt. Các bạn hãy tạo một hàm để xử lý nó nhé:

```jsx
client.on('messageCreate', (message) => {
    console.log(message);
});
```

Khi một tin nhắn được gửi đến, event “**messageCreate**” sẽ được kích hoạt và trả về một object tên là “**message**” lưu các thông tin về tin nhắn đó. Chúng ta truyền object này vào đoạn code bên trong ngoặc nhọn và in nó ra màn hình xem nó có những cái gì. Các bạn hãy bấm chạy code, đợi con bot login xong và gửi một tin nhắn bất kỳ vào kênh chat:

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 28.png" alt="Untitled 28.png"></p>

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 29.png" alt="Untitled 29.png"></p>


Các bạn có thể thấy Discord trả về rất nhiều thông tin về tin nhắn mình vừa gửi, bao gồm ID mà tin đó được gửi, ID người gửi, thời gian gửi, ... . Để con bot phản hồi tin nhắn “**Ping**”, chúng ta cần kiểm tra xem nội dung tin nhắn đó có phải “**Ping**” không:

```jsx
client.on('messageCreate', (message) => {
    if (message.content == "Ping"){
        
    }
});
```

Chúng ta truy cập nội dung tin nhắn bằng **message.content**. Nếu nội dung đúng là “**Ping**”, con Bot sẽ gửi một tin nhắn “**Pong**” vào cùng kênh chat đó. Chúng ta truy cập vào kênh chat của một tin nhắn được gửi bằng **`message.channel`** và gửi tin nhắn vào đó bằng **`message.channel.send(”Pong”)`**:

```jsx
client.on('messageCreate', (message) => {
    if (message.content == "Ping"){
        message.channel.send("Pong");
    }
});
```

Oke Ctrl+S để lưu code và chạy thôi:

```jsx
require('dotenv').config();

const {
    Client,
    Intents,
} = require('discord.js');
const { Player } = require('discord-player');

const client = new Client({ intents: [
    Intents.FLAGS.GUILDS,
    Intents.FLAGS.GUILD_MESSAGES,
    Intents.FLAGS.GUILD_VOICE_STATES,
    "GUILD_MEMBERS",
] });

const player = new Player(client);

client.on('ready', () => {
    console.log('minccino ready!');
});

client.on('messageCreate', (message) => {
    if (message.content == "Ping"){
        message.channel.send("Pong");
    }
}); 

client.login(process.env.DISCORD_TOKEN);
```

<p style="text-align: center;"><img src="/assets/images/posts/2022-05-01-discord-music-bot-2/Untitled 30.png" alt="Untitled 30.png"></p>

Quá tuyệt vời! Vậy là các bạn đã lập trình cho Bot xử lý tin nhắn mà người dùng gửi đến. Trong bài viết tiếp theo, UCC sẽ cùng bạn lập trình các tính năng chơi nhạc cho Bot nhé! Hãy đón chờ nha!