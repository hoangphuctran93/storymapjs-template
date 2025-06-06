# Tài Liệu Tổng Hợp Dự Án StoryMapJS Template

## 1. Thông tin tổng quan

-   **Mô tả dự án:** Tùy biến StoryMapJS Template với hệ thống logo header có logic fallback và second footer credit.
-   **Ngày bắt đầu:** 2025-06-02
-   **Ngày cập nhật cuối:** 2025-06-03
-   **Công nghệ sử dụng:** Jekyll, HTML, CSS, JavaScript, Python, GitHub Actions.
-   **Tiến độ hoàn thành:** Hoàn thành

## 2. Yêu cầu dự án (Requirements)

-   Tùy biến StoryMapJS Template với hệ thống logo header có logic fallback.
-   Thêm second footer credit.
-   Tùy biến favicon của trang.
-   max-height của navbar là 90px.
-   logo image max-height là 65px.
-   Tuỳ chỉnh logic navbar-brand-text là false (ẩn khi có logo).
-   Đảm bảo mã nguồn có thể deploy được trên github page.

## 3. Giải pháp áp dụng (Solutions)

-   Sử dụng cấu trúc modular với các file cấu hình YAML riêng biệt (config_base.yml, config_header.yml, config_footer.yml, config_theme.yml) để dễ dàng tùy chỉnh và bảo trì.
-   Sử dụng script Python (merge_configs.py) để merge các file cấu hình vào file cấu hình chính của Jekyll (`_temp/_config.yml`), đảm bảo không ảnh hưởng đến hệ thống collections.
-   Tạo các template header và footer credit mới (_includes/header.html, _includes/footer-credit.html) để tùy chỉnh giao diện.
-   Cập nhật GitHub Actions workflow (.github/workflows/jekyll.yml) để tự động chạy script merge_configs.py và build trang web với cấu hình đã merge.
-   Sử dụng CSS variables để tùy chỉnh kiểu dáng của header và footer credit.

## 4. Cấu trúc dự án

```
├── configs/                    # Config modular (MỚI)
│   ├── config_base.yml        # Bổ sung cho Jekyll (không ảnh hưởng collections)
│   ├── config_header.yml      # Header + logo
│   ├── config_footer.yml      # Footer credit
│   └── config_theme.yml       # Theme extensions
├── scripts/                   # Python merger system (MỚI)
│   ├── merge_configs.py
│   └── config_merger/
├── collections/               # GIỮ NGUYÊN collections system
│   ├── education.md
│   └── tourism.md
├── _plugins/                  # GIỮ NGUYÊN collection generator
│   └── collection_generator.rb
├── _temp/                     # File config tạm (MỚI)
│   └── _config.yml
└── .github/workflows/         # CẬP NHẬT workflow
    └── jekyll.yml
```

## 5. Chi tiết từng file code

### _config.yml
**Đường dẫn:** /_config.yml
**Mục đích:** Cấu hình chính của Jekyll, bao gồm các thiết lập cơ bản cho trang web, URL, và các plugins.

### .github/workflows/jekyll.yml
**Đường dẫn:** /.github/workflows/jekyll.yml
**Mục đích:** Workflow của GitHub Actions để tự động build và triển khai trang web Jekyll lên GitHub Pages.

### configs/config_base.yml
**Đường dẫn:** /configs/config_base.yml
**Mục đích:** Cấu hình bổ sung cho Jekyll, bao gồm các thiết lập SEO, social media, và navigation. File này không thay đổi cấu hình collections system.

### configs/config_header.yml
**Đường dẫn:** /configs/config_header.yml
**Mục đích:** Cấu hình header và logo của trang web, bao gồm các thiết lập về hình ảnh, branding, và kiểu dáng.

### configs/config_footer.yml
**Đường dẫn:** /configs/config_footer.yml
**Mục đích:** Cấu hình footer credit của trang web, bao gồm các thiết lập về thông tin nhà phát triển, nhà tài trợ, kiểu dáng, và layout.

### configs/config_theme.yml
**Đường dẫn:** /configs/config_theme.yml
**Mục đích:** Cấu hình theme bổ sung cho trang web, bao gồm các thiết lập về typography, effects, spacing, và custom colors.

### scripts/merge_configs.py
**Đường dẫn:** /scripts/merge_configs.py
**Mục đích:** Script Python để merge các file cấu hình YAML vào file cấu hình chính của Jekyll (`_config.yml`), đồng thời đảm bảo tính tương thích với hệ thống collections.

### _includes/header.html
**Đường dẫn:** /_includes/header.html
**Mục đích:** Template cho header của trang web, bao gồm logo, các mục điều hướng, và các thiết lập kiểu dáng.

### _includes/footer-credit.html
**Đường dẫn:** /_includes/footer-credit.html
**Mục đích:** Template cho footer credit của trang web, hiển thị thông tin về nhà phát triển và nhà tài trợ.

### _layouts/default.html
**Đường dẫn:** /_layouts/default.html
**Mục đích:** Layout mặc định của trang web, xác định cấu trúc chung của trang, bao gồm header, content, và footer.

## 6. Hướng dẫn cho developer
## 7. Changelog và milestones

## 8. Done List

-   [ ] Đã đọc và phân tích tất cả file.
-   [ ] Đã tổng hợp đầy đủ code tối ưu.
-   [ ] Đã tạo hướng dẫn setup chi tiết.
-   [ ] Đã lưu file vào dev-documents/header-footer-credit.
-   [ ] Đã tạo backups cho tất cả file cấu hình và template.
-   [ ] Đã kiểm tra tính đầy đủ và chính xác của tài liệu.