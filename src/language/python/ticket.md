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

    
    
