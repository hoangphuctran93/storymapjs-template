### _layouts/default.html
**Đường dẫn:** /_layouts/default.html
**Mục đích:** Layout mặc định của trang web, xác định cấu trúc chung của trang, bao gồm header, content, và footer.

```html
<!DOCTYPE html>
<html lang="en" class="h-100">
    <head>
        {% include template/head.html %}
    </head>
    <body class="d-flex flex-column h-100">
        <div id="skip-to-content"><a href="#maincontent">Skip to main content</a></div>
        {% include header.html %}
        <main id="maincontent" role="main" aria-label="Content" class="flex-shrink-0">
        {{ content }}
        </main>
        {% include template/footer.html %}
        {% include footer-credit.html %}
        {% include template/foot.html %}
    </body>
</html>
```

**Ghi chú code:**

*   `<!DOCTYPE html>`: Khai báo loại tài liệu HTML5.
*   `<html lang="en" class="h-100">`: Khai báo thẻ HTML với ngôn ngữ tiếng Anh và class `h-100` để chiếm toàn bộ chiều cao trang.
*   `<head>`: Chứa các thông tin metadata của trang web.
    *   `{% include template/head.html %}`: Include template cho phần head của trang web.
*   `<body class="d-flex flex-column h-100">`: Thẻ body với các class Bootstrap để tạo layout linh hoạt.
    *   `<div id="skip-to-content"><a href="#maincontent">Skip to main content</a></div>`: Liên kết để bỏ qua phần điều hướng và đi thẳng đến nội dung chính.
    *   `{% include header.html %}`: Include template cho header của trang web.
    *   `<main id="maincontent" role="main" aria-label="Content" class="flex-shrink-0">`: Phần nội dung chính của trang web.
        *   `{{ content }}`: Nội dung của từng trang cụ thể.
    *   `{% include template/footer.html %}`: Include template cho footer của trang web (collections footer).
    *   `{% include footer-credit.html %}`: Include template cho footer credit (thông tin nhà phát triển và nhà tài trợ).
    *   `{% include template/foot.html %}`: Include template cho phần foot của trang web (các script và thư viện JavaScript).
