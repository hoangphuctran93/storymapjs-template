### configs/config_theme.yml
**Đường dẫn:** /configs/config_theme.yml
**Mục đích:** Cấu hình theme bổ sung cho trang web, bao gồm các thiết lập về typography, effects, spacing, và custom colors.

```yaml
# ===================================================================
# CẤU HÌNH THEME BỔ SUNG - TƯƠNG THÍCH VỚI COLLECTIONS STYLING
# ===================================================================

theme_extensions:
  # Typography (không ảnh hưởng collections)
  typography:
    font_family_primary: "Inter, -apple-system, BlinkMacSystemFont, sans-serif"
    font_family_heading: "Inter, sans-serif"
    font_weight_normal: "400"
    font_weight_medium: "500"
    font_weight_semibold: "600"
    font_weight_bold: "700"
    
  # Effects (tương thích với collections)
  effects:
    transition_base: "0.3s"
    transition_fast: "0.15s"
    border_radius_sm: "0.25rem"
    border_radius_md: "0.5rem"
    border_radius_lg: "0.75rem"
    shadow_sm: "0 1px 2px 0 rgba(0, 0, 0, 0.05)"
    shadow_md: "0 4px 6px -1px rgba(0, 0, 0, 0.1)"
    shadow_lg: "0 10px 15px -3px rgba(0, 0, 0, 0.1)"
    
  # Spacing (không conflict với collections)
  spacing:
    container_max_width: "1200px"
    section_padding: "4rem 0"
    grid_gap: "1.5rem"
    
  # Custom colors (bổ sung cho collections colors)
  custom_colors:
    header_primary: "#2563eb"
    header_secondary: "#1e40af"
    footer_bg: "#374151"
    credit_developer: "#fbbf24"
    credit_sponsor: "#60a5fa"
```

**Ghi chú code:**

*   `theme_extensions`: Cấu hình các theme extensions.
    *   `typography`: Cấu hình typography của trang web.
        *   `font_family_primary`: Font chữ chính của trang web.
        *   `font_family_heading`: Font chữ cho các heading.
        *   `font_weight_normal`: Độ đậm của chữ thường.
        *   `font_weight_medium`: Độ đậm của chữ vừa.
        *   `font_weight_semibold`: Độ đậm của chữ bán đậm.
        *   `font_weight_bold`: Độ đậm của chữ đậm.
    *   `effects`: Cấu hình các hiệu ứng của trang web.
        *   `transition_base`: Thời gian transition cơ bản.
        *   `transition_fast`: Thời gian transition nhanh.
        *   `border_radius_sm`: Border radius nhỏ.
        *   `border_radius_md`: Border radius vừa.
        *   `border_radius_lg`: Border radius lớn.
        *   `shadow_sm`: Hiệu ứng đổ bóng nhỏ.
        *   `shadow_md`: Hiệu ứng đổ bóng vừa.
        *   `shadow_lg`: Hiệu ứng đổ bóng lớn.
    *   `spacing`: Cấu hình khoảng cách của trang web.
        *   `container_max_width`: Chiều rộng tối đa của container.
        *   `section_padding`: Khoảng cách padding của section.
        *   `grid_gap`: Khoảng cách giữa các grid item.
    *   `custom_colors`: Cấu hình các màu tùy chỉnh.
        *   `header_primary`: Màu chính của header.
        *   `header_secondary`: Màu phụ của header.
        *   `footer_bg`: Màu nền của footer.
        *   `credit_developer`: Màu của developer credit.
        *   `credit_sponsor`: Màu của sponsor credit.
