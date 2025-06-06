### configs/config_header.yml
**Đường dẫn:** /configs/config_header.yml
**Mục đích:** Cấu hình header và logo của trang web, bao gồm các thiết lập về hình ảnh, branding, và kiểu dáng.

```yaml
# ===================================================================
# CẤU HÌNH HEADER VÀ LOGO - TƯƠNG THÍCH COLLECTIONS
# ===================================================================

header:
  # === LOGO CONFIGURATION ===
  logo:
    image: "/assets/img/logo-expquangngai.png"
    alt: "StoryMap Logo"
    height: "100%"
    width: "auto"
    max_height: "65px"
    link: "/"
    show: true
    
  # === BRANDING LOGIC ===
  branding:
    show_navbar_brand: false      # true: hiển thị cả logo và brand text
    show_title: true
    show_subtitle: true          # Hiển thị subtitle
    fallback_to_brand: true      # Fallback khi không có logo
    
  # === HEADER STYLING ===
  styling:
    navbar_class: "navbar-dark"
    background_color: "#2563eb"
    background_gradient: "linear-gradient(135deg, #2563eb, #1e40af)"
    text_color: "#ffffff"
    link_color: "#ffffff"
    link_hover_color: "#fbbf24"
    sticky: true
    shadow: "0 2px 4px rgba(0,0,0,0.1)"
    max_height: "90px"
    
  # === MOBILE SETTINGS ===
  mobile:
    breakpoint: "lg"
    toggle_position: "right"
```

**Ghi chú code:**

*   `header`: Cấu hình header của trang web.
    *   `logo`: Cấu hình logo của trang web.
        *   `image`: Đường dẫn đến hình ảnh logo.
        *   `alt`: Văn bản thay thế cho hình ảnh logo.
        *   `height`: Chiều cao của hình ảnh logo.
        *   `width`: Chiều rộng của hình ảnh logo.
        *   `max_height`: Chiều cao tối đa của hình ảnh logo.
        *   `link`: Liên kết khi click vào logo.
        *   `show`: Hiển thị logo hay không.
    *   `branding`: Cấu hình branding của trang web.
        *   `show_navbar_brand`: Hiển thị cả logo và brand text hay không.
        *   `show_title`: Hiển thị title hay không.
        *   `show_subtitle`: Hiển thị subtitle hay không.
        *   `fallback_to_brand`: Sử dụng brand text khi không có logo hay không.
    *   `styling`: Cấu hình kiểu dáng của header.
        *   `navbar_class`: Class của navbar (ví dụ: "navbar-dark").
        *   `background_color`: Màu nền của header.
        *   `background_gradient`: Gradient nền của header.
        *   `text_color`: Màu chữ của header.
        *   `link_color`: Màu liên kết của header.
        *   `link_hover_color`: Màu liên kết khi hover của header.
        *   `sticky`: Hiệu ứng sticky cho header hay không.
        *   `shadow`: Hiệu ứng đổ bóng cho header.
        *   `max_height`: Chiều cao tối đa của header.
    *   `mobile`: Cấu hình cho thiết bị di động.
        *   `breakpoint`: Breakpoint để chuyển sang giao diện mobile.
        *   `toggle_position`: Vị trí của nút toggle menu.
