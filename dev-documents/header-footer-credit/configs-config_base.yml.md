### configs/config_base.yml
**Đường dẫn:** /configs/config_base.yml
**Mục đích:** Cấu hình bổ sung cho Jekyll, bao gồm các thiết lập SEO, social media, và navigation. File này không thay đổi cấu hình collections system.

```yaml
# ===================================================================
# CẤU HÌNH BỔ SUNG - KHÔNG THAY ĐỔI COLLECTIONS SYSTEM
# Chỉ thêm các cấu hình mới, giữ nguyên collections config
# ===================================================================

# === SEO BỔ SUNG (không ảnh hưởng collections) ===
seo:
  type: Organization
  name: "StoryMap Template"
  links:
    - https://facebook.com/storymaps
    - https://instagram.com/storymaps

# === SOCIAL MEDIA (bổ sung) ===
social:
  facebook: "https://facebook.com/storymaps"
  instagram: "https://instagram.com/storymaps"
  youtube: "https://youtube.com/storymaps"
  twitter: "https://twitter.com/storymaps"

# === NAVIGATION (bổ sung cho header) ===
nav_items:
  - title: "Home"
    url: "/"
  - title: "Collections"
    url: "/collections/"
  - title: "About"
    url: "/about/"

# LƯU Ý: KHÔNG thêm collections config ở đây để tránh conflict
# Collections config sẽ được giữ nguyên trong _config.yml gốc
```

**Ghi chú code:**

*   `seo`: Cấu hình các thông tin SEO cho trang web.
    *   `type`: Loại hình tổ chức (ví dụ: "Organization").
    *   `name`: Tên của tổ chức (ví dụ: "StoryMap Template").
    *   `links`: Các liên kết đến các trang mạng xã hội.
*   `social`: Cấu hình các liên kết đến các trang mạng xã hội.
    *   `facebook`: Liên kết đến trang Facebook.
    *   `instagram`: Liên kết đến trang Instagram.
    *   `youtube`: Liên kết đến kênh YouTube.
    *   `twitter`: Liên kết đến trang Twitter.
*   `nav_items`: Cấu hình các mục điều hướng trên header.
    *   `title`: Tiêu đề của mục điều hướng.
    *   `url`: Đường dẫn của mục điều hướng.
