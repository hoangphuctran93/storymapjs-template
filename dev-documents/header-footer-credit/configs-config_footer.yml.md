### configs/config_footer.yml
**Đường dẫn:** /configs/config_footer.yml
**Mục đích:** Cấu hình footer credit của trang web, bao gồm các thiết lập về thông tin nhà phát triển, nhà tài trợ, kiểu dáng, và layout.

```yaml
# ===================================================================
# CẤU HÌNH FOOTER CREDIT - KHÔNG ẢNH HƯỞNG COLLECTIONS
# ===================================================================

footer_credit:
  enabled: true
  
  # === DEVELOPER CREDIT ===
  developer:
    name: "AgentC Asia"
    url: "https://agentc.asia"
    show_icon: true
    description: "Phát triển và vận hành"
    logo: "/assets/images/agentc-logo.png"
    show_logo: false
    
  # === SPONSOR CREDIT ===
  sponsor:
    name: "Cộng đồng hỗ trợ doanh nghiệp Quảng Ngãi .Org"
    url: ""
    description: "Tài trợ bởi"
    show_support_text: true
    
  # === STYLING ===
  styling:
    background_color: "#374151"
    text_color: "#ffffff"
    developer_link_color: "#fbbf24"
    sponsor_text_color: "#60a5fa"
    border_top: "1px solid #4b5563"
    padding: "1rem 0"
    font_size: "0.875rem"
    
  # === LAYOUT ===
  layout:
    developer_position: "left"
    sponsor_position: "right"
    stack_on_mobile: true
```

**Ghi chú code:**

*   `footer_credit`: Cấu hình footer credit của trang web.
    *   `enabled`: Bật/tắt hiển thị footer credit.
    *   `developer`: Cấu hình thông tin nhà phát triển.
        *   `name`: Tên của nhà phát triển.
        *   `url`: URL của nhà phát triển.
        *   `show_icon`: Hiển thị icon liên kết hay không.
        *   `description`: Mô tả về nhà phát triển.
        *   `logo`: Đường dẫn đến logo của nhà phát triển.
        *   `show_logo`: Hiển thị logo của nhà phát triển hay không.
    *   `sponsor`: Cấu hình thông tin nhà tài trợ.
        *   `name`: Tên của nhà tài trợ.
        *   `url`: URL của nhà tài trợ.
        *   `description`: Mô tả về nhà tài trợ.
        *   `show_support_text`: Hiển thị text hỗ trợ hay không.
    *   `styling`: Cấu hình kiểu dáng của footer credit.
        *   `background_color`: Màu nền của footer credit.
        *   `text_color`: Màu chữ của footer credit.
        *   `developer_link_color`: Màu liên kết của nhà phát triển.
        *   `sponsor_text_color`: Màu chữ của nhà tài trợ.
        *   `border_top`: Đường viền trên của footer credit.
        *   `padding`: Khoảng cách padding của footer credit.
        *   `font_size`: Kích thước chữ của footer credit.
    *   `layout`: Cấu hình layout của footer credit.
        *   `developer_position`: Vị trí của thông tin nhà phát triển (ví dụ: "left", "right", "center").
        *   `sponsor_position`: Vị trí của thông tin nhà tài trợ (ví dụ: "left", "right", "center").
        *   `stack_on_mobile`: Stack các thành phần trên thiết bị di động hay không.
