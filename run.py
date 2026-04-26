# -*- coding: utf-8 -*-
"""
应用入口文件
启动Flask开发服务器
"""
import os
from app import create_app

# 创建应用实例
app = create_app(os.environ.get('FLASK_CONFIG', 'development'))

if __name__ == '__main__':
    # 确保数据目录存在
    os.makedirs('data', exist_ok=True)
    os.makedirs(os.path.join('app', 'static', 'uploads'), exist_ok=True)

    print("=" * 60)
    print("  出国（境）学习交流项目展示系统")
    print("  访问地址: http://127.0.0.1:5000")
    print("=" * 60)

    app.run(host='0.0.0.0', port=5000, debug=True)
