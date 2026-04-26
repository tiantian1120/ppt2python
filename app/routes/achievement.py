"""
成果展示路由模块
处理竞赛成果、专利软著等展示路由
"""
from flask import Blueprint, render_template, request
from app import db
from app.models.models import Achievement

achievement_bp = Blueprint('achievement', __name__)


@achievement_bp.route('/')
def achievement_list():
    """成果列表页 - 支持分类筛选"""
    category = request.args.get('category', '')
    level = request.args.get('level', '')

    query = Achievement.query
    if category:
        query = query.filter_by(category=category)
    if level:
        query = query.filter_by(level=level)

    achievements = query.order_by(Achievement.created_at.desc()).all()

    # 获取所有分类用于筛选
    categories = db.session.query(Achievement.category).distinct().all()
    levels = db.session.query(Achievement.level).distinct().all()

    return render_template('pages/achievement/list.html',
                           achievements=achievements,
                           categories=[c[0] for c in categories if c[0]],
                           levels=[l[0] for l in levels if l[0]],
                           current_category=category,
                           current_level=level)


@achievement_bp.route('/<int:achievement_id>')
def achievement_detail(achievement_id):
    """成果详情页"""
    achievement = Achievement.query.get_or_404(achievement_id)
    return render_template('pages/achievement/detail.html',
                           achievement=achievement)
