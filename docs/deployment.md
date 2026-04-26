# 出国（境）学习交流项目展示系统 - 部署文档

## 1. 项目概述

本系统是基于Flask框架开发的"粤港澳大湾区人工智能与跨学科创新实践访学项目"展示网站，用于展示出国（境）学习交流项目的相关信息，包括项目介绍、学习计划、参访安排、成果展示、个人档案和申请指南等功能模块。

### 1.1 技术栈

| 组件 | 技术选型 | 版本 |
|------|---------|------|
| 后端框架 | Flask | 3.0+ |
| ORM | Flask-SQLAlchemy | 3.1+ |
| 数据库 | SQLite | 3.x |
| 前端模板 | Jinja2 | 3.1+ |
| CSS框架 | 自定义CSS | - |
| JavaScript | 原生JS | ES6+ |
| 图标库 | Font Awesome | 6.5+ |
| 字体 | Noto Sans SC (Google Fonts) | - |

### 1.2 系统要求

- Python 3.8+
- pip 包管理器
- 操作系统：Windows / macOS / Linux

## 2. 项目结构

```
study_exchange_system/
├── app/                          # 应用主目录
│   ├── __init__.py               # 应用包初始化
│   ├── config.py                 # 配置文件
│   ├── factory.py                # 应用工厂
│   ├── models/                   # 数据模型
│   │   ├── __init__.py
│   │   └── models.py             # 数据库模型定义
│   ├── routes/                   # 路由模块
│   │   ├── __init__.py
│   │   ├── main.py               # 主页路由
│   │   ├── project.py            # 项目路由
│   │   ├── achievement.py        # 成果路由
│   │   ├── profile.py            # 个人档案路由
│   │   └── guide.py              # 申请指南路由
│   ├── templates/                # 模板文件
│   │   ├── base.html             # 基础模板
│   │   ├── components/           # 组件模板
│   │   └── pages/                # 页面模板
│   │       ├── index.html        # 首页
│   │       ├── about.html        # 关于
│   │       ├── contact.html      # 联系我们
│   │       ├── 404.html          # 404页面
│   │       ├── 500.html          # 500页面
│   │       ├── project/          # 项目相关页面
│   │       ├── achievement/      # 成果相关页面
│   │       ├── profile/          # 个人档案页面
│   │       └── guide/            # 申请指南页面
│   └── static/                   # 静态资源
│       ├── css/
│       │   └── style.css         # 主样式表
│       ├── js/
│       │   └── main.js           # 主脚本
│       ├── images/               # 图片资源
│       └── uploads/              # 上传文件
├── data/                         # 数据目录
│   ├── init_db.py                # 数据库初始化脚本
│   └── study_exchange.db         # SQLite数据库文件
├── tests/                        # 测试目录
│   ├── __init__.py
│   └── test_models.py            # 单元测试
├── docs/                         # 文档目录
├── run.py                        # 应用入口
├── requirements.txt              # 依赖清单
└── README.md                     # 项目说明
```

## 3. 安装部署

### 3.1 获取代码

```bash
# 克隆或下载项目到本地
cd /path/to/your/workspace
```

### 3.2 创建虚拟环境（推荐）

```bash
# 创建虚拟环境
python3 -m venv venv

# 激活虚拟环境
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

### 3.3 安装依赖

```bash
pip install -r requirements.txt
```

### 3.4 初始化数据库

```bash
python3 data/init_db.py
```

执行成功后会看到：
```
✓ 数据表创建成功
✓ 示例数据填充完成
```

### 3.5 启动开发服务器

```bash
python3 run.py
```

启动后访问：http://127.0.0.1:5000

## 4. 生产环境部署

### 4.1 使用 Gunicorn 部署

```bash
# 安装 Gunicorn
pip install gunicorn

# 启动服务（4个工作进程）
gunicorn -w 4 -b 0.0.0.0:8000 "app:create_app('production')"
```

### 4.2 使用 Nginx 反向代理

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /static/ {
        alias /path/to/study_exchange_system/app/static/;
        expires 30d;
    }
}
```

### 4.3 使用 systemd 管理服务

创建 `/etc/systemd/system/study-exchange.service`：

```ini
[Unit]
Description=Study Exchange System
After=network.target

[Service]
User=www-data
Group=www-data
WorkingDirectory=/path/to/study_exchange_system
Environment="PATH=/path/to/venv/bin"
ExecStart=/path/to/venv/bin/gunicorn -w 4 -b 127.0.0.1:8000 "app:create_app('production')"

[Install]
WantedBy=multi-user.target
```

```bash
# 启动服务
sudo systemctl start study-exchange
sudo systemctl enable study-exchange
```

## 5. 配置说明

### 5.1 环境变量

| 变量名 | 说明 | 默认值 |
|--------|------|--------|
| FLASK_CONFIG | 运行环境配置 | default |
| SECRET_KEY | 密钥（生产环境务必修改） | study-exchange-system-secret-key-2026 |

### 5.2 配置模式

| 模式 | 说明 |
|------|------|
| development | 开发模式，开启DEBUG |
| testing | 测试模式，使用内存数据库 |
| production | 生产模式，关闭DEBUG |

## 6. 运行测试

```bash
# 运行所有测试
python3 -m unittest discover tests -v

# 运行指定测试文件
python3 -m unittest tests.test_models -v
```

## 7. 常见问题

### Q: 数据库初始化失败？
A: 确保 `data/` 目录存在且有写入权限。

### Q: 端口被占用？
A: 修改 `run.py` 中的端口号，或使用环境变量：
```bash
FLASK_RUN_PORT=8080 python3 run.py
```

### Q: 如何重置数据库？
A: 删除 `data/study_exchange.db` 文件后重新运行 `python3 data/init_db.py`。
