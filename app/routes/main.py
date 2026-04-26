"""
主页路由模块
处理首页、关于页面等核心路由
"""
from flask import Blueprint, render_template
from app.models.models import Project, Achievement, StudentProfile, Motivation, ExpectedOutcome

main_bp = Blueprint('main', __name__)


@main_bp.route('/')
def index():
    """首页 - 展示项目概览、精选成果、个人简介"""
    # 获取主项目信息
    project = Project.query.filter_by(category='main').first()
    # 获取精选成果
    featured_achievements = Achievement.query.filter_by(is_featured=True).limit(6).all()
    # 获取学生档案
    profile = StudentProfile.query.first()
    # 获取参与动机
    motivations = Motivation.query.order_by(Motivation.sort_order).all()
    # 获取预期成果
    outcomes = ExpectedOutcome.query.order_by(ExpectedOutcome.sort_order).all()
    # 统计数据
    stats = {
        'national_awards': Achievement.query.filter_by(level='国家级').count(),
        'provincial_awards': Achievement.query.filter_by(level='省级').count(),
        'total_achievements': Achievement.query.count(),
        'patents': Achievement.query.filter(
            Achievement.category.in_(['专利', '软著'])
        ).count(),
    }

    return render_template('pages/index.html',
                           project=project,
                           featured_achievements=featured_achievements,
                           profile=profile,
                           motivations=motivations,
                           outcomes=outcomes,
                           stats=stats)


@main_bp.route('/about')
def about():
    """关于页面"""
    return render_template('pages/about.html')


@main_bp.route('/contact')
def contact():
    """联系我们页面"""
    return render_template('pages/contact.html')
