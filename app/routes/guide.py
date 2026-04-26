"""
申请指南路由模块
处理申请流程、材料清单等路由
"""
from flask import Blueprint, render_template

guide_bp = Blueprint('guide', __name__)


@guide_bp.route('/')
def guide_index():
    """申请指南首页"""
    return render_template('pages/guide/index.html')


@guide_bp.route('/process')
def application_process():
    """申请流程页"""
    return render_template('pages/guide/process.html')


@guide_bp.route('/materials')
def required_materials():
    """申请材料清单页"""
    return render_template('pages/guide/materials.html')


@guide_bp.route('/faq')
def faq():
    """常见问题页"""
    return render_template('pages/guide/faq.html')
