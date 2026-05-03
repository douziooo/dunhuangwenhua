#!/usr/bin/env python3
"""
批量修复 Vue 文件中的静态资源路径，适配 GitHub Pages 子目录部署。
将 /images/xxx /video/xxx /audio/xxx 替换为动态路径。
"""

import os
import re
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(SCRIPT_DIR, 'src', 'views')

# 匹配模板中的 src="/images/... src="/video/... src="/audio/...
# 包括 <img src=" <source src=" <video src=" <img :src=" 等形式
TEMPLATE_PATTERN = re.compile(
    r'((?:src|poster|:src|:poster)\s*=\s*)'  # 属性名和等号
    r'(?:'
    r'"(/(?:images|video|audio)/[^"]*)"'       # 双引号
    r"|"
    r"'(/(?:images|video|audio)/[^']*)'"       # 单引号
    r')',
    re.DOTALL
)

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 1. 在 <script setup> 中注入 baseURL 和 assetUrl（如果还没有）
    if 'const baseURL' not in content and 'assetUrl' not in content:
        # 在 import NavBar 之后注入
        content = re.sub(
            r"(import NavBar from ['\"].*?['\"]\n)",
            r"\nconst baseURL = import.meta.env.BASE_URL || '/'\n"
            r"const assetUrl = (path) => path.startsWith('/') ? baseURL + path.slice(1) : path\n\n"
            r"\1",
            content
        )
    
    # 2. 修复模板中的 src="/images/... 等
    def replace_path(match):
        prefix = match.group(1)  # src= 或 :src= 等
        path1 = match.group(2)   # 双引号内的路径
        path2 = match.group(3)   # 单引号内的路径
        
        path = path1 or path2
        
        # 已经是 assetUrl() 的不再替换
        if path.startswith('assetUrl('):
            return match.group(0)
        
        return f'{prefix}assetUrl("{path}")'
    
    content = TEMPLATE_PATTERN.sub(replace_path, content)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'  ✅ 已修复: {os.path.basename(filepath)}')
        return True
    else:
        print(f'  ⏭  无需修改: {os.path.basename(filepath)}')
        return False

def main():
    print('🔧 开始批量修复静态资源路径...\n')
    
    if not os.path.isdir(SRC_DIR):
        print(f'❌ 目录不存在: {SRC_DIR}')
        sys.exit(1)
    
    vue_files = sorted([
        os.path.join(SRC_DIR, f) for f in os.listdir(SRC_DIR)
        if f.endswith('.vue')
    ])
    
    modified = 0
    for filepath in vue_files:
        if fix_file(filepath):
            modified += 1
    
    print(f'\n✅ 完成！共修复 {modified} 个文件。')

if __name__ == '__main__':
    main()
