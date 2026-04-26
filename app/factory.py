"""
Flask应用工厂模块
负责创建和配置Flask应用实例
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import config

# 初始化扩展
db = SQLAlchemy()


def create_app(config_name='default'):
    """
    应用工厂函数
    :param config_name: 配置名称 (development/testing/production)
    :return: Flask应用实例
    """
    app = Flask(__name__)

    # 加载配置
    app.config.from_object(config[config_name])

    # 初始化扩展
    db.init_app(app)

    # 注册蓝图（路由）
    from app.routes.main import main_bp
    from app.routes.project import project_bp
    from app.routes.achievement import achievement_bp
    from app.routes.profile import profile_bp
    from app.routes.guide import guide_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(project_bp, url_prefix='/project')
    app.register_blueprint(achievement_bp, url_prefix='/achievement')
    app.register_blueprint(profile_bp, url_prefix='/profile')
    app.register_blueprint(guide_bp, url_prefix='/guide')

    # 注册错误处理
    register_error_handlers(app)

    return app


def register_error_handlers(app):
    """注册自定义错误处理"""
    @app.errorhandler(404)
    def page_not_found(e):
        from flask import render_template
        return render_template('pages/404.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        from flask import render_template
        return render_template('pages/500.html'), 500
