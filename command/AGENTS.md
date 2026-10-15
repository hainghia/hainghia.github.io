# AGENTS.md — `projects/hainghia.github.io/command`

## Export CV PDF

- `just resume-pdf` xuất riêng bản EN từ `src/resume/index.html` bằng Python API của WeasyPrint 68.0; không cần trình duyệt, Playwright hoặc server HTTP.
- Mặc định ghi `exports/resume/hainghia-cv-en.pdf` dưới project, bị gitignore; có thể truyền đường dẫn PDF khác. Đường dẫn tương đối tính từ project kể cả khi gọi wrapper ở root monorepo.
- Giữ CSS bản in của HTML, bổ sung khổ A4. Nút print và chuyển ngôn ngữ được ẩn qua `.no-print`.
- CSS riêng cho PDF dùng cỡ chữ 10pt và block thay các flex column lồng nhau để tránh layout quá chậm trong WeasyPrint. Phần đầu giữ sidebar 1/3 và summary 2/3 bằng float + margin; phần kinh nghiệm trở lại toàn chiều rộng. Không sửa HTML website.
- Khi export, URL ảnh `https://hainghia.github.io/images/` (kể cả dấu slash kép) được ánh xạ về `src/images/` có sẵn; HTML nguồn không bị sửa, quá trình render không tải ảnh qua mạng.
- `uv` tải dependency vào môi trường tách biệt qua `--no-project --with`, không sửa manifest/lock cũ của project. Máy cần Pango và font hệ thống; Ubuntu dùng `libpango-1.0-0`, `libpangoft2-1.0-0`; macOS dùng `brew install pango`.
- Nguồn cài đặt: https://doc.courtbouillon.org/weasyprint/v68.0/first_steps.html

> **Vai trò:** _(chưa mô tả — điền tay/AI; vùng này sync-safe)_

<!-- TREE:AUTO:BEGIN -->
- **Loại:** Just automation
- **Thư mục con:** common, github, mdbook
- **File:** .DS_Store, `__init__.just`
- **Bối cảnh:** [`projects/hainghia.github.io/AGENTS.md`](../AGENTS.md)
<!-- TREE:AUTO:END -->
