"""
个人档案路由模块
处理学生个人档案展示路由
"""
from flask import Blueprint, render_template
from app.models.models import StudentProfile, Achievement

profile_bp = Blueprint('profile', __name__)


@profile_bp.route('/')
def profile_detail():
    """个人档案详情页"""
    profile = StudentProfile.query.first_or_404()
    # 获取相关成果
    achievements = Achievement.query.order_by(Achievement.created_at.desc()).limit(10).all()

    # 统计数据
    stats = {
        'national': Achievement.query.filter_by(level='国家级').count(),
        'provincial': Achievement.query.filter_by(level='省级').count(),
        'school': Achievement.query.filter_by(level='校级').count(),
        'patent': Achievement.query.filter(
            Achievement.category.in_(['专利', '软著'])
        ).count(),
    }

    return render_template('pages/profile/detail.html',
                           profile=profile,
                           achievements=achievements,
                           stats=stats)
