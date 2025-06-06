#!/usr/bin/env python3
import yaml
import sys
import os

def validate_footer_config():
    """Validate footer system configuration"""
    config_path = "configs/config_footer.yml"
    
    print("🔍 Validating footer system configuration...")
    
    # Kiểm tra file tồn tại
    if not os.path.exists(config_path):
        print("⚠️  Footer system config not found, using defaults")
        return True
    
    try:
        # Đọc file config footer system
        with open(config_path, 'r', encoding='utf-8') as f:
            footer_config = yaml.safe_load(f)
        
        if not footer_config:
            print("❌ Config file is empty")
            return False
        
        # Kiểm tra các section bắt buộc (logic của bạn)
        required_sections = ['footer_main', 'footer_copyright', 'footer_credit', 'footer_global']
        missing_sections = []
        
        for section in required_sections:
            if section not in footer_config:
                missing_sections.append(section)
        
        if missing_sections:
            for section in missing_sections:
                print(f'❌ Missing required section: {section}')
            return False
        
        # Logic validation của bạn (đã tối ưu)
        if 'navigation_columns' in footer_config['footer_main']:
            columns = footer_config['footer_main']['navigation_columns']
            print(f'✅ Footer navigation: {len(columns)} columns configured')
        
        if footer_config['footer_main'].get('social_media', {}).get('enabled', False):
            social_count = len(footer_config['footer_main']['social_media'].get('links', []))
            print(f'✅ Social media: {social_count} platforms configured')
        
        print('✅ Footer system config validation passed')
        return True
        
    except yaml.YAMLError as e:
        print(f'❌ YAML parsing error: {e}')
        return False
    except Exception as e:
        print(f'❌ Validation error: {e}')
        return False

if __name__ == "__main__":
    success = validate_footer_config()
    sys.exit(0 if success else 1)
