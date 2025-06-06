### _includes/footer-credit.html
**Đường dẫn:** /_includes/footer-credit.html
**Mục đích:** Template cho footer credit của trang web, hiển thị thông tin về nhà phát triển và nhà tài trợ.

```html
<!-- ===================================================================
SECOND FOOTER CREDIT - KHÔNG ẢNH HƯỞNG COLLECTIONS FOOTER
Thêm vào cuối trang sau footer chính của collections
=================================================================== -->

{% if site.footer_credit.enabled %}
<div id="credit-footer" class="py-3">
  <div class="container">
    <div class="row align-items-center{% if site.footer_credit.layout.stack_on_mobile %} flex-column flex-md-row{% endif %}">

      <!-- Developer Credit -->
      <div class="col-md-6 text-{{ site.footer_credit.layout.developer_position | default: 'center' }} text-md-{{ site.footer_credit.layout.developer_position | default: 'start' }}">
        <small class="credit-text">
          <strong>{{ site.footer_credit.developer.description | default: 'Phát triển và vận hành' }}:</strong>

          {% if site.footer_credit.developer.url %}
            <a href="{{ site.footer_credit.developer.url }}" target="_blank"
               class="credit-link text-decoration-none"
               style="color: var(--credit-developer-link-color);"
               rel="noopener noreferrer">
              {% if site.footer_credit.developer.show_icon %}<i class="fas fa-external-link-alt me-1"></i>{% endif %}
              {{ site.footer_credit.developer.name }}
            </a>
          {% else %}
            <span style="color: var(--credit-developer-link-color);">
              {{ site.footer_credit.developer.name }}
            </span>
          {% endif %}

          {% if site.footer_credit.developer.show_logo and site.footer_credit.developer.logo %}
            <img src="{{ site.footer_credit.developer.logo }}"
                 alt="{{ site.footer_credit.developer.name }}"
                 style="height: 20px; margin-left: 8px; vertical-align: middle;"
                 loading="lazy">
          {% endif %}
        </small>
      </div>

      <!-- Sponsor Credit -->
      <div class="col-md-6 text-{{ site.footer_credit.layout.sponsor_position | default: 'center' }} text-md-{{ site.footer_credit.layout.sponsor_position | default: 'end' }}">
        <small class="credit-text">
          <strong>{{ site.footer_credit.sponsor.description | default: 'Tài trợ bởi' }}:</strong>

          {% if site.footer_credit.sponsor.url %}
            <a href="{{ site.footer_credit.sponsor.url }}" target="_blank"
               class="credit-link text-decoration-none"
               style="color: var(--credit-sponsor-text-color);"
               rel="noopener noreferrer">
              {{ site.footer_credit.sponsor.name }}
            </a>
          {% else %}
            <span style="color: var(--credit-sponsor-text-color);">
              {{ site.footer_credit.sponsor.name }}
            </span>
          {% endif %}
        </small>
      </div>

    </div>
  </div>
</div>

<!-- CSS không ảnh hưởng collections styling -->
<style>
  :root {
    --footer-bg-color: {{ site.footer_credit.styling.background_color | default: '#374151' }};
    --footer-text-color: {{ site.footer_credit.styling.text_color | default: '#ffffff' }};
    --credit-developer-link-color: {{ site.footer_credit.styling.developer_link_color | default: '#fbbf24' }};
    --credit-sponsor-text-color: {{ site.footer_credit.styling.sponsor_text_color | default: '#60a5fa' }};
    --transition-base: {{ site.theme_extensions.effects.transition_base | default: '0.3s' }};
  }

  #credit-footer {
    transition: all var(--transition-base) ease;
    margin-top: 0; /* Không tạo gap với footer chính */
    background-color: var(--footer-bg-color);
    border-top: {{ site.footer_credit.styling.border_top | default: '1px solid #4b5563' }};
    font-size: {{ site.footer_credit.styling.font_size | default: '0.875rem' }};
  }

  .credit-link {
    transition: all var(--transition-base) ease;
    display: inline-block;
  }

  .credit-link:hover {
    transform: translateY(-1px);
    text-shadow: 0 2px 4px rgba(0,0,0,0.3);
  }

  .credit-text {
    line-height: 1.5;
    color: var(--footer-text-color);
  }

  /* Responsive design */
  {% if site.footer_credit.layout.stack_on_mobile %}
  @media (max-width: 768px) {
    #credit-footer .col-md-6 {
      text-align: center !important;
      margin-bottom: 0.5rem;
    }

    #credit-footer .col-md-6:last-child {
      margin-bottom: 0;
    }
  }

  @media (max-width: 576px) {
    .credit-text {
      font-size: 0.8rem !important;
    }
  {% endif %}
</style>
{% endif %}
