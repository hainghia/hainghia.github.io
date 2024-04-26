# Interview

- Bạn có thể giải thích hoạt động của Virtual DOM trong React không?

> Virtual DOM trong React là một cấu trúc dữ liệu nhẹ giúp theo dõi các thay đổi trong DOM thực. Khi có sự thay đổi
> trong state hoặc props, React tạo ra một Virtual DOM mới và so sánh nó với Virtual DOM cũ để xác định những phần nào cần
> cập nhật trên DOM thực.

- Bạn có thể so sánh giữa == và === trong JavaScript không?

> Trong JavaScript, `==` là toán tử so sánh bằng, nó sẽ chuyển đổi kiểu dữ liệu trước khi so sánh. Trong khi đó, `===`
> là toán tử so sánh tuyệt đối, nó sẽ so sánh cả giá trị và kiểu dữ liệu.

- Bạn có thể giải thích về Event Loop trong JavaScript không?

> Event Loop trong JavaScript là một cơ chế cho phép JavaScript thực hiện các tác vụ không đồng bộ mà không cần đa
> luồng. Nó liên tục kiểm tra call stack để xem có công việc nào cần thực hiện không. Nếu call stack trống, nó sẽ lấy công
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
> hoặc Mocha. Kiểm tra đơn vị tập trung vào việc kiểm tra một phần nhỏ của mã (thường là một hàm), trong khi kiểm tra tích
> hợp kiểm tra cách các phần của mã tương tác với nhau.