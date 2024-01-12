# Ticket

#### [Sự cố khi cài đặt confluent-kafka trên chip `arm64`](https://github.com/confluentinc/confluent-kafka-python/issues/1466#issuecomment-1378377378)

Choice version > `2.3.0`

#### Xoá toàn bộ package đã cài trong Python và chỉ giữ lại package hệ thống

    ```shell
    pip3 freeze | xargs pip3 uninstall -y
    pip3 freeze | grep -v "@" | xargs pip3 uninstall -y
    
    pip3 install --upgrade pip
    ```

#### [Lỗi Shadows built-in name 'id'](https://docs.python.org/3/library/functions.html#id)

    > Lỗi này liên quan đến việc đặt tên biến giống với một từ khóa hoặc một hàm có sẵn trong Python. Trong trường hợp này, "id" là một hàm có sẵn trong Python để lấy địa chỉ bộ nhớ của một đối tượng. Khi bạn đặt tên biến là "id", Python sẽ coi nó là một hàm và sẽ báo lỗi.

#### [Hiển thị danh sách routes trong `Chalice`](https://aws.github.io/chalice/topics/routing.html)

Thêm đoạn code sau vào file `list_routes.py`

```python

import os

from app import app
from tabulate import tabulate


def list_routes():
    table_data = []
    for path, route_info in app.routes.items():
        for method, route_entry in route_info.items():
            authorizer = route_entry.authorizer
            name = route_entry.view_name
            project_root = os.getcwd()
            file = os.path.relpath(route_entry.view_function.__code__.co_filename, project_root)

            table_data.append([path, method, authorizer, name, file])
    table_headers = ["Endpoint", "Method", "Authorizer", "Name", "Path"]

    table = tabulate(table_data, headers=table_headers, tablefmt="grid")

    csv_file_path = "./routes.csv"

    # with open(csv_file_path, "w", newline="") as csv_file:
    #     writer = csv.writer(csv_file)
    #     writer.writerow(table_headers)
    #     writer.writerows(table_data)

    print(f"Dữ liệu đã được xuất ra file CSV: {csv_file_path}")

    print(table)
```

`app.py`

```python
list_routes()
```

### Celery Tasks run multiple times

> Celery tự động tái tạo lại task chưa được chạy

`Visibility timeout` Nếu một `task` không được `acknowledged` trong thời gian chờ hiển thị (`Visibility timeout`) thì task đó sẽ được phân phối lại `redelivered` cho một worker và được thực thi.
Điều này gây ra sự cố với các tác vụ `ETA/countdown/retry tasks` trong đó thời gian thực thi vượt quá thời gian chờ hiển thị, nó sẽ được thực thi lại và lặp lại trong một vòng lặp.
Để khắc phục có thể tăng `Visibility timeout` để phù hợp với thời gian của `ETA/countdown/retry tasks` dài nhất.
**Tuy nhiên, điều này không được khuyến khích vì `Visibility timeout` lâu sẽ chỉ trì hoãn việc gửi lại các task 'BỊ MẤT' trong trường hợp failure hoặc terminated workers.**
Broker không phải là database, vì vậy nếu bạn cần lập lịch các tác vụ trong tương lai xa hơn, tác vụ định kỳ dựa trên database-backed có thể là lựa chọn tốt hơn. Các tác vụ định kỳ sẽ không bị ảnh hưởng bởi `visibility timeout` vì đây là một khái niệm tách biệt với `ETA/countdown/retry tasks`

- [Celery documentation Visibility Timeout](https://docs.celeryq.dev/en/stable/getting-started/backends-and-brokers/redis.html#visibility-timeout)

The default visibility timeout for Redis is 1 hour.

```python
app.conf.broker_transport_options = {'visibility_timeout': 3600}  # 1 hour.
```

> Flower is an open-source web application for monitoring and managing Celery clusters.
- [Flower](https://flower.readthedocs.io/en/latest/install.html)
- [Tasks run multiple times groups.google.com](https://groups.google.com/g/celery-users/c/W0Qf09ahjas?pli=1)

Flower sẽ `monitoring` and `managing` Celery do đó nó sẽ giúp tái tạo những task bị mất của Celery. Điều này vô tình khiến cho một task chưa hoàn tất nhưng hết `Visibility timeout` sẽ được tái tạo lại.
Và đó là nguyên nhân chính gây ra lỗi một task được lên lịch và chạy nhiều lần.

```
[2024-01-12 10:47:37,888: INFO/MainProcess] Task worker.offer.delay_update_offer_end_date[c524b552-e6e7-44ea-ba1e-fa71c187f2f2] received
[2024-01-12 10:48:29,443: INFO/MainProcess] Task worker.offer.delay_update_offer_end_date[c524b552-e6e7-44ea-ba1e-fa71c187f2f2] received
[2024-01-12 10:50:09,347: INFO/MainProcess] Task worker.offer.delay_update_offer_end_date[c524b552-e6e7-44ea-ba1e-fa71c187f2f2] received
```
