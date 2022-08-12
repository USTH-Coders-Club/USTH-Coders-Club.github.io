---
layout: post
title: "Một số concepts cơ bản của React"
author: [tungngt]
categories: [coding]
tags: [code]
image: assets\images\posts\2022-08-12-concept-co-ban-react\banner.png
description: "Trước đây các trang web chỉ được làm bằng HTML, CSS, JS. Nhưng một nhược điểm khi chỉ dùng đơn thuần HTML, CSS, JS là khó có thể tạo ra những trang web với độ tương tác cao. Để giải quyết vấn đề đó đã có nhiều JS frontend library đã ra đời giúp nâng cao tính tương tác và biến các trang web giống các native app hơn. Một trong số chúng là: React, Vue, Svelte,… Trong số những thư viện đó, React là thư viện được sử dụng nhiều nhất.

Đối với các bạn đang bắt đầu học React, sẽ có nhiều thay đổi so với sử dụng HTML, CSS, JS bình thường, cùng với đó là nhiều concepts mới. Vì vậy bài viết này sẽ giải thích về một số concepts cơ bản khi sử dụng thư viện này. Bài viết này không phải là hướng dẫn cụ thể cách sử dụng React; mà là một tài liệu tham khảo cho các bạn đang học React, muốn tránh cảm thấy ngợp cũng như muốn có một cái nhìn tổng quát hơn về thư viện này."
featured: true  
toc: true
---

Trước đây các trang web chỉ được làm bằng HTML, CSS, JS. Nhưng một nhược điểm khi chỉ dùng đơn thuần HTML, CSS, JS là khó có thể tạo ra những trang web với độ tương tác cao. Để giải quyết vấn đề đó đã có nhiều JS frontend library đã ra đời giúp nâng cao tính tương tác và biến các trang web giống các native app hơn. Một trong số chúng là: React, Vue, Svelte,… Trong số những thư viện đó, React là thư viện được sử dụng nhiều nhất.

Đối với các bạn đang bắt đầu học React, sẽ có nhiều thay đổi so với sử dụng HTML, CSS, JS bình thường, cùng với đó là nhiều concepts mới. Vì vậy bài viết này sẽ giải thích về một số concepts cơ bản khi sử dụng thư viện này. Bài viết này không phải là hướng dẫn cụ thể cách sử dụng React; mà là một tài liệu tham khảo cho các bạn đang học React, muốn tránh cảm thấy ngợp cũng như muốn có một cái nhìn tổng quát hơn về thư viện này.

## React là gì?

- React là một một thư viện JavaScript open-source được phát triển bởi Facebook.
- React được dùng để xây dựng UI (user interfaces) cho các trang web.
- React đơn giản hóa việc xây dựng UI bằng cách chia nó thành những Component nhỏ, có thể tái sử dụng.

## JSX

Thường một trang web sẽ được viết trong các file HTML và JS riêng biệt. Một nhược điểm khi viết HTML và JS riêng biệt đó là bạn phải viết trực tiếp (hard code) những thông tin bạn muốn hiển thị trong file HTML. Khi muốn sử dụng các chức năng của JS, và truy cập HTML bạn phải sử dụng query: 

```jsx
const container = document.querySelector(".container")
```

Hay khi muốn thêm các element mới phải viết:

```jsx
const paragraph = document.createElement("p")
container.appendChild(paragraph)
```

Viết code như vậy rất tốn thời gian.

Trong React, JSX giúp kết hợp JS và HTML ngay trong một file JS. Ví dụ bạn có thế tạo một tag <h1> ngay trong file JS:

```jsx
const title = <h1>Hello, World!</h1>
```

Ở đây `<h1>Hello, World!</h1>` được gọi là một đoạn JSX.

!!!LƯU Ý: các đoạn JSX phải có một parent tag và khi viết xuống dòng phải bọc trong “()”

đúng:

```jsx
// sai
const element = <p>paragraph 1</p><p>paragraph 2</p>

// đúng 
const element = <div><p>paragraph 1</p><p>paragraph 2</p><div>

// sai  
const element = 
	<div>
		<p>paragraph 1</p>
		<p>paragraph 2</p>
	</div>

// đúng 
const element = (
	<div>
		<p>paragraph 1</p>
		<p>paragraph 2</p>
	</div>
);
```

Ngoài ra để tránh sử dụng nhiều tag <div> thừa, ta có thể dùng React Fragment: <></> để bọc các thông tin

```jsx
const element = (
	<>
		<p>paragraph 1</p>
		<p>paragraph 2</p>
	</>
);
```

Nhìn qua, JSX trông khá giống với các đoạn HTML bình thường. Nhưng JSX có một tính đặc biệt đó là cho phép ta embed các đoạn JavaScript vào trong bằng cách bọc chúng trong ngoặc nhọn “{}”. Trong ví dụ dưới, chúng ta khai báo biến name và dùng nó trong đoạn JSX:

```jsx
const name = 'React';
const element = <h1>Hello, { name }</h1>;

// element bằng <h1>Hello, React</h1>
```

Chúng ta cũng có thể gọi các hàm:

```jsx
function sum(a, b) return a + b;

const element = <p>1 + 2 = { sum(1, 2) }</p>;

// element bằng <p>1 + 2 = 3</p>
```

JSX cũng có thể được lưu trong một Array:

```jsx
const names = ["React", "John", "Mike", "Amy"]
const helloList = names.map((name, index) => <h1 key={index}>Hello {name}</h1>)
const hello = <div>{helloList}</div>;
```

!!!LƯU Ý: các element JSX trong một Array phải có attribute key khác nhau.

## Component.

Một trong những tính năng nổi tiếng của React đó là có thể sử dụng Component. Đây là là một tính năng rất hữu ích và quan trọng mà bạn cần nắm chắc khi sử dụng React. Component đơn giản là những phần nhỏ của một trang web hay một UI. Component cho phép bạn chia UI thành các thành phần nhỏ hơn, độc lập và có thể tái sử dụng như những miếng Lego vậy.

Lấy ví dụ như như trang web UCC Blog:


<p style="text-align: center;"><img src="/assets/images/posts/2022-08-12-concept-co-ban-react/khung_unedited.jpg" alt="khung_unedited.jpg"></p>

Với HTML bình thường, chúng ta có thể biểu diễn nó như sau:

```html
<div>
	<div>
		<img src="image1.jpg" />
		<h3>Phân tích lỗ hổng</h3>
		<p>Hôm nay UCC sẽ đổi gió…</p>
		<p>Đỗ Nhật Thành</p>
	</div>
	<div>
		<img src="image2.jpg" />
		<h3>Làm thế nào để giải quyết…</h3>
		<p>Giải quyết các bài toán…</p>
		<p>Nguyễn Thanh Tùng</p>
	</div>
	<div>
		<img src="image3.jpg" />
		<h3>So sánh GUI và CLI…</h3>
		<p>Hệ điều hành là…</p>
		<p>Phạm Minh Hiếu, Văn Quốc An</p>
	</div>
</div>
```

Quan sát kỹ hơn, ta có thể thấy cấu trúc của các bài Post khá tương tự nhau. Các bài Posts (như ô bôi đỏ trong hình dưới) đều có cách sắp xếp thông tin giống nhau:

<p style="text-align: center;"><img src="/assets/images/posts/2022-08-12-concept-co-ban-react/khung.jpg" alt="khung.jpg"></p>

Hay trong file HTML chúng có dạng:

```html
<div>
	<img src="image.jpg" />
	<h3>Tiêu đề</h3>
	<p>Nội dung</p>
	<p>Tác giả</p>
</div>
```

Thay vì phải viết lặp đi lặp lại đoạn HTML trên; chúng ta có thể tách bài Post thành một Component và sử dụng chúng nhiều lần:

```jsx
function Post() {
	return (
		<div>
			<img src="image.jpg" />
			<h3>Tiêu đề</h3>
			<p>Nội dung</p>
			<p>Tác giả</p>
		</div>
	);
}
```

Component trong React đơn giản là một function có tên ở dạng [PascalCase](https://techterms.com/definition/pascalcase) (viết hoa các chữ cái đầu của từ). Function này sẽ trả về một đoạn JSX mà nó muốn hiển thị. Như ví dụ ở trên, để tách bài Post thành một Component, chúng ta tạo một function với tên Post và trả lại đoạn JSX với cấu trúc của bài Post.

Sau khi đã tạo xong Component, ta có thể sử dụng chúng như những tag HTML:

```html
const postsList= (
	<div>
		<Post/>
		<Post/>
		<Post/>
	</div>
)
```

Với cách viết trên, bạn có thể đã nhận ra các Component Post đều sẽ hiển thị ra màn hình thông tin giống nhau. Vậy làm thể nào để một Component hiển thị những thông tin khác nhau?

### Props

Props sẽ giúp ta đạt được điều này. Các Component có thể nhận thêm parameter props:

```jsx
function Hello(props) {
	return <h1>Hello {props.name}</h1>;
}
```

Props là những thông tin cần thiết để một Component có thể hiển thị đúng. Khi thông tin trong props thay đổi, Component sẽ thay đổi để hiển thị chính xác. Props có thể được truyền cho Component bằng cách khai báo thêm các attributes khi sử dụng Component đó:

```jsx
const helloUCC = <Hello name="UCC" />
// helloUCC bằng <h1>Hello UCC</h1>
```

Quay lại với Component Post ta có thể thay những dữ liệu cố định (hard-coded value) thành những dữ liệu được lấy từ props:

```jsx
function Post(props) {
	return (
		<div>
			<img src={props.thumbnail} />
			<h3>{props.title}</h3>
			<p>{props.description}</p>
			<p>{props.author}</p>
		</div>
	);
}
```

và thêm các attributes:

```jsx
const postsList= (
	<div>
		<Post title="Phân tích…" author="Thành" description="Hôm nay…" thumbnail="image1.jpg" />
		<Post title="So sánh…" author="Hiếu, An" description="Hệ điều…" thumbnail="image2.jpg" />
		<Post title="Làm thế…" author="Tùng" description="Giải quyết…" thumbnail="image3.jpg"/>
	</div>
)
```

Một property hữu ích của props là children:

```jsx
function Link(props) {
	return (
		<a href={props.href}>{props.children}</a>
	)
}
```

Props.children là những thông tin được đặt giữa open và closing tag của một Component:

```jsx
const link1 = (
	<Link href="reactjs.org/docs"><h1>React docs</h1></Link>
)

// link1 bằng <a href="reactjs.org/docs"><h1>React docs</h1></a>
```

## Xử lý các Events

Việc xử lý các events trong React cũng khá tương tự với . Nhưng có một số khác biệt về syntax:

- Các events trong React sử dụng camelCase (viết thường chữ đầu tiên và viết hoa chữ đầu tiên các từ sau). Ví dụ: onclick ⇒ onClick, onchange ⇒ onChange

Ta có thể pass các hàm để xử lý các events: 

```jsx
function HelloButton() {

	function hello() {
		console.log("hello")
	}

	return <button onClick={hello}>say hello</button>
}
```

!!!LƯU Ý: bạn cần pass một hàm, chứ không phải invoke nó.

```jsx
// sai    
const HelloButton = () => <button onClick={hello()}>say hello</button>

// đúng
const HelloButton = () => <button onClick={hello}>say hello</button>
```

Để thêm các các input cho hàm, bạn có thể tạo một [anonymous function](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) 

```jsx
function HelloButton() {

	function hello(name) {
		console.log("hello " + name)
	}

	return (
		<button 
			onClick={ () => hello("React") }
		>
			say hello
		</button>);
}
```

## State (trạng thái)

Trong một trang web, UI sẽ có những Component với với các trạng thái khác nhau. Ví dụ như một cái Counter (đếm số) sẽ có trạng thái là số hiện tại:

<p style="text-align: center;"><img src="/assets/images/posts/2022-08-12-concept-co-ban-react/Untitled.png" alt="Untitled.png"></p>
Khi cần dùng đến state, chúng ta có thể sử dụng hàm useState của React:

```jsx
const [state, setState] = useState(initialValue);
```

- Hàm useState sẽ trả về một Array với 2 giá trị:
    - Giá trị thứ nhất chính là biết chứa state hiện tại.
    - Giá trị thứ hai là hàm để thay đổi state đó.
- Ta có thể thêm giá trị ban đầu khi của một state khi gọi `useState(initialValue)`.
- Theo convention, ta sẽ đặt tên hàm để thay đổi state giống với state đó và thêm “set” ở đằng trước và viết hoa chữ tiếp theo. Ví dụ bạn muốn lưu một email: `const [email, setEmail] = useState("")`.

Quay trở lại với ví dụ một cái Counter, chúng ta có thể tạo Component như sau:

```jsx
function Counter() {
	const [count, setCount] = useState(0);
	return (
		<div>
			<h1>Counter</h1>
			<button onClick={() => setCount(count + 1)}>+</button>
			<p>{count}</p>
			<button onClick={() => setCount(count - 1)}>-</button>
		</div>
	);
}
```

Ta thêm một state gọi là count và khởi tạo nó với giá 0. Ta dùng nó biến count để hiển thị số đếm hiện tại trong tag <p>. Sau đó ta thêm hai nút và nghe Event onClick để tăng và giảm số đếm hiện tại.

!!!LƯU Ý: Khi dùng useState, không được thay đổi biến được trả về đó mà phải dùng hàm thay đổi state. Trong ví dụ trên nếu dùng `onClick={count++}`; số đếm hiện ra màn hình sẽ không thay đổi. Ta phải dùng `setCount(count + 1)`.

## **Controlled Component**

Controlled Component thường được dùng với những tag như <form>, &lt;input&gt;, &lt;textarea&gt;, &lt;select&gt;,… Để kiểm soát những tag như vậy trong React, ta có thể dùng Controlled Component.

Ví dụ:

```jsx
function EmailInput() {
	const [email, setEmail] = useState("")
	
	const handleChange = (event) => {
		setEmail(event.target.value)
	}

	return <input type="email" value={email} onChange={handleChange}/>
}
```

Ta có thể tạo một state để lưu giá trị email mà người dùng nhập. Ta gắn biến email atribut value của tag &lt;input&gt;. Đồng thời nghe Event onChange để update giá trị email khi người dùng nhập vào ô input.

Để ngăn các hành động mặc định của browser bạn có thể dùng `preventDefault()`

```jsx
function EmailInput() {
	const [email, setEmail] = useState("")
	const [password, setPassword] = useState("")

	const handleSubmit = (event) => {
		event.preventDefault();
		console.log(email);
		console.log(password);
	}

	return (
		<form onSubmit={handleSubmit}>
			<input type="email" value={email} onChange={ e => setEmail(event.target.value) } />
			<input type="password" value={password} onChange={ e => setPassword(event.target.value) } />
			<button type="submit">Sign In</button>
		</form>
	);
}
```

Ví dụ như `preventDefault()` ở đây sẽ tránh browser add thêm query vào url và reload trang.

## Tham khảo thêm

- Documentation của React khá đầy đủ và hữu ích. Bạn có thể đọc thêm phần [Main Concepts](https://reactjs.org/docs) để hiểu thêm về các Concepts khác trong React.
- [React Tutorial của Mosh Hamedani](https://www.youtube.com/watch?v=Ke90Tje7VS0)

## Tổng kết

React là một library open-source với cộng đồng sử dụng lớn. Có rất nhiều bài viết, video, tutorial về React. Chính vì vậy khi sử dụng React, nhất là khi mới bắt đầu học, đừng ngần ngại lên mạng tra khi có câu hỏi. Bởi vì những câu hỏi đó khả năng cao là đã được trả lời. Từ đó các bạn có thể tích lũy cho minh những kiến thức mới về thư viện này.

Cảm ơn các bạn đã đọc bài viết. Nhớ theo dõi UCC Blog để đón đọc các bài viết mới nhé!