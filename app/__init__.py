"""
出国（境）学习交流项目展示系统
基于Flask框架开发的粤港澳大湾区人工智能与跨学科创新实践访学项目展示网站
"""

__version__ = '1.0.0'
__author__ = 'Study Exchange System'

# 从工厂模块导入核心组件
from app.factory import create_app, db  # noqa: F401, E402
