# Interview

- Bạn có thể giải thích hoạt động của Virtual DOM trong React không?

> Virtual DOM trong React là một cấu trúc dữ liệu nhẹ giúp theo dõi các thay đổi trong DOM thực. Khi có sự thay đổi
> trong state hoặc props, React tạo ra một Virtual DOM mới và so sánh nó với Virtual DOM cũ để xác định những phần nào
> cần
> cập nhật trên DOM thực.

- Bạn có thể so sánh giữa == và === trong JavaScript không?

> Trong JavaScript, `==` là toán tử so sánh bằng, nó sẽ chuyển đổi kiểu dữ liệu trước khi so sánh. Trong khi đó, `===`
> là toán tử so sánh tuyệt đối, nó sẽ so sánh cả giá trị và kiểu dữ liệu.

- Bạn có thể giải thích về Event Loop trong JavaScript không?

> Event Loop trong JavaScript là một cơ chế cho phép JavaScript thực hiện các tác vụ không đồng bộ mà không cần đa
> luồng. Nó liên tục kiểm tra call stack để xem có công việc nào cần thực hiện không. Nếu call stack trống, nó sẽ lấy
> công
> việc đầu tiên từ hàng đợi callback và đẩy nó vào call stack.

- Bạn có thể giải thích về hoisting trong JavaScript không?

> Hoisting trong JavaScript là hành vi mặc định của JavaScript, nơi nó chuyển các khai báo lên đầu của phạm vi hiện tại
> trước khi thực thi mã.

- Bạn có thể giải thích về closures trong JavaScript không?

> Closures trong JavaScript là một hàm có quyền truy cập vào biến nằm ngoài phạm vi của nó, bao gồm cả biến toàn cục và
> biến trong hàm bao quanh nó.

- Bạn có thể giải thích về Promises và async/await trong JavaScript không?

> Promises và async/await trong JavaScript là cơ chế để xử lý các tác vụ không đồng bộ. Promises là một đối tượng đại
> diện cho kết quả cuối cùng của một tác vụ không đồng bộ và trạng thái của nó. Async/await là cú pháp ngọt ngào để làm
> việc với Promises một cách dễ dàng hơn.

- Bạn có thể giải thích về Hooks trong React không?

> Hooks trong React là một tính năng cho phép bạn sử dụng state và các tính năng khác của React mà không cần tạo một
> class component. Các hooks phổ biến bao gồm useState, useEffect, và useContext.

- Bạn có thể giải thích về Redux và cách nó hoạt động không?

> Redux là một thư viện quản lý trạng thái ứng dụng JavaScript. Nó giúp bạn quản lý trạng thái toàn cục của ứng dụng của
> mình trong một cấu trúc dữ liệu duy nhất và cho phép trạng thái được cập nhật theo cách dự đoán được thông qua các hàm
> reducer.

- Bạn có thể giải thích về CSS Box Model không?

> CSS Box Model là một mô hình hộp mà tất cả các phần tử HTML đều tuân theo khi được render trên trình duyệt. Nó bao
> gồm: content, padding, border và margin.

- Bạn có thể giải thích về CSS Flexbox và Grid không?

> CSS Flexbox và Grid là hai công cụ hiện đại trong CSS giúp bạn dễ dàng thiết kế layout cho trang web của mình. Flexbox
> tốt cho việc sắp xếp các phần tử theo một chiều, trong khi Grid tốt cho việc sắp xếp các phần tử theo hai chiều.

- Bạn có thể giải thích về cách sử dụng Webpack không?

> Webpack là một công cụ module bundler cho JavaScript. Nó lấy các tệp nguồn của bạn, biến đổi chúng và kết hợp chúng
> thành một tệp (hoặc nhiều tệp) mà bạn có thể sử dụng trong trang web của mình.

- Bạn có thể giải thích về TypeScript và lợi ích của nó không?

> TypeScript là một ngôn ngữ lập trình mạnh mẽ hơn dựa trên JavaScript. Nó bổ sung thêm các tính năng như kiểu dữ liệu
> tĩnh và các tính năng hướng đối tượng, giúp việc phát triển ứng dụng lớn trở nên dễ dàng hơn.

- Bạn có thể giải thích về cách xử lý lỗi trong JavaScript không?

> Xử lý lỗi trong JavaScript thường được thực hiện bằng cách sử dụng cấu trúc try/catch. Bạn đặt đoạn mã có thể gây ra
> lỗi trong khối try, và nếu có lỗi xảy ra, nó sẽ được bắt trong khối catch.

- Bạn có thể giải thích về cách tối ưu hiệu suất trang web không?

> Tối ưu hiệu suất trang web có thể bao gồm nhiều kỹ thuật khác nhau, bao gồm minification và uglification của mã, tối
> ưu hóa hình ảnh, sử dụng lazy loading, và sử dụng Service Workers và caching.

- Bạn có thể giải thích về cách thực hiện kiểm tra đơn vị và kiểm tra tích hợp trong JavaScript không?

> Kiểm tra đơn vị và kiểm tra tích hợp trong JavaScript thường được thực hiện bằng cách sử dụng các thư viện như Jest
> hoặc Mocha. Kiểm tra đơn vị tập trung vào việc kiểm tra một phần nhỏ của mã (thường là một hàm), trong khi kiểm tra
> tích
> hợp kiểm tra cách các phần của mã tương tác với nhau.

- Bạn có thể giải thích về cách hoạt động của Event Delegation trong JavaScript không?

> Event Delegation trong JavaScript là một cơ chế cho phép bạn gán các sự kiện listener cho một phần tử cha thay vì gán
> chúng cho từng phần tử con. Khi một sự kiện được kích hoạt trên một phần tử con, nó sẽ nổi lên và được xử lý bởi
> listener trên phần tử cha.

- Bạn có thể giải thích về cách hoạt động của Shadow DOM trong Web Components không?

> Shadow DOM là một cơ chế trong Web Components cho phép bạn tạo ra một DOM riêng biệt, được cô lập từ DOM chính. Điều
> này giúp giảm thiểu sự xung đột giữa các phần tử và tạo ra các thành phần có thể tái sử dụng.

- Bạn có thể giải thích về cách hoạt động của CSS Preprocessors như SASS hoặc LESS không?

> CSS Preprocessors như SASS hoặc LESS là công cụ giúp viết CSS một cách dễ dàng hơn bằng cách cung cấp các tính năng
> như biến, hàm, mixins, và lồng.

- Bạn có thể giải thích về cách hoạt động của CSS Modules không?

> CSS Modules là một cơ chế cho phép bạn viết CSS trong các tệp riêng biệt và sau đó import chúng vào JavaScript. Điều
> này giúp giảm thiểu sự xung đột giữa các lớp CSS và tăng tính module hóa của mã.

- Bạn có thể giải thích về cách hoạt động của CSS-in-JS không?

> CSS-in-JS là một kỹ thuật cho phép bạn viết CSS trực tiếp trong JavaScript. Điều này giúp tăng tính module hóa và cung
> cấp khả năng sử dụng các tính năng của JavaScript như biến và hàm trong CSS.

- Bạn có thể giải thích về cách hoạt động của HTTP/2 và cách nó cải thiện hiệu suất không?

> HTTP/2 là phiên bản mới nhất của giao thức truyền tải siêu văn bản (HTTP). Nó cung cấp nhiều cải tiến so với HTTP/1.1,
> bao gồm việc hỗ trợ đa luồng, nén tiêu đề, và đẩy máy chủ, giúp cải thiện hiệu suất trang web.

- Bạn có thể giải thích về cách hoạt động của Web Sockets không?

> Web Sockets là một công nghệ cho phép thiết lập một kết nối hai chiều giữa máy khách và máy chủ. Điều này cho phép cả
> hai có thể gửi và nhận dữ liệu mà không cần yêu cầu lại.

- Bạn có thể giải thích về cách hoạt động của GraphQL không?

> GraphQL là một ngôn ngữ truy vấn dữ liệu được phát triển bởi Facebook. Nó cho phép bạn yêu cầu chính xác những dữ liệu
> bạn cần, giúp giảm bớt lượng dữ liệu không cần thiết được truyền qua mạng.

- Bạn có thể giải thích về cách hoạt động của Web Assembly không?

> Web Assembly (Wasm) là một dạng mã máy nhị phân được thiết kế để được thực thi nhanh trên các trình duyệt web. Nó cho
> phép bạn chạy mã viết bằng các ngôn ngữ khác như C, C++, và Rust trên trình duyệt.

- Bạn có thể giải thích về cách hoạt động của IndexedDB không?

> IndexedDB là một API lưu trữ dữ liệu phía máy khách cho phép bạn lưu trữ dữ liệu lớn, bao gồm cả dữ liệu có cấu trúc,
> trên trình duyệt của người dùng.

- Bạn có thể giải thích về cách hoạt động của Service Workers và cách chúng được sử dụng để tạo Progressive Web Apps
  không?

> Service Workers là một loại script chạy ngầm trên trình duyệt, cho phép các tính năng không đồng bộ như lấy dữ liệu từ
> cache, đẩy thông báo, và đồng bộ hóa dữ liệu nền. Chúng là một phần quan trọng trong việc tạo ra Progressive Web
> Apps (
> PWA).

- Bạn có thể giải thích về cách hoạt động của Intersection Observer API không?

> Intersection Observer API cung cấp một cách để theo dõi việc một phần tử giao cắt với một phần tử cha hoặc viewport.
> Điều này hữu ích cho các tác vụ như tải lười (lazy loading) hình ảnh hoặc xây dựng các menu cuộn dính.

- Bạn có thể giải thích về cách hoạt động của requestAnimationFrame không?

> requestAnimationFrame là một phương thức cho phép bạn thực hiện các hoạt động hoạt hình trơn tru trên trình duyệt. Nó
> hoạt động bằng cách lên lịch một hàm để được gọi ngay trước khi trình duyệt tiếp theo vẽ màn hình.

- Bạn có thể giải thích về cách hoạt động của WebRTC không?

> WebRTC (Web Real-Time Communication) là một công nghệ cho phép truyền tải dữ liệu trực tiếp giữa các trình duyệt, hỗ
> trợ các ứng dụng như video chat mà không cần plugin hoặc bên thứ ba.

- Bạn có thể giải thích về cách hoạt động của SVG và cách sử dụng nó trong việc tạo đồ họa trên web không?

> SVG (Scalable Vector Graphics) là một định dạng hình ảnh vector dựa trên XML cho phép bạn tạo ra đồ họa phức tạp có
> thể mở rộng mà không mất chất lượng.