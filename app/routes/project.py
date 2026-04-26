"""
项目展示路由模块
处理项目介绍、学习计划、参访计划等路由
"""
from flask import Blueprint, render_template
from app.models.models import Project, LearningModule, VisitPlan

project_bp = Blueprint('project', __name__)


@project_bp.route('/')
def project_list():
    """项目列表页"""
    projects = Project.query.order_by(Project.created_at.desc()).all()
    return render_template('pages/project/list.html', projects=projects)


@project_bp.route('/<int:project_id>')
def project_detail(project_id):
    """项目详情页"""
    project = Project.query.get_or_404(project_id)
    modules = LearningModule.query.filter_by(
        project_id=project_id
    ).order_by(LearningModule.sort_order).all()
    return render_template('pages/project/detail.html',
                           project=project,
                           modules=modules)


@project_bp.route('/learning-plan')
def learning_plan():
    """学习计划页 - 展示四大学习模块"""
    # 获取主项目的学习模块
    project = Project.query.filter_by(category='main').first()
    if project:
        modules = LearningModule.query.filter_by(
            project_id=project.id
        ).order_by(LearningModule.sort_order).all()
    else:
        modules = []

    return render_template('pages/project/learning_plan.html', modules=modules)


@project_bp.route('/visit-plan')
def visit_plan():
    """参访计划页 - 展示企业/高校参访安排"""
    visits = VisitPlan.query.order_by(VisitPlan.sort_order).all()
    return render_template('pages/project/visit_plan.html', visits=visits)


@project_bp.route('/motivation')
def motivation():
    """参与动机页"""
    from app.models.models import Motivation
    motivations = Motivation.query.order_by(Motivation.sort_order).all()
    return render_template('pages/project/motivation.html', motivations=motivations)


@project_bp.route('/expected-outcomes')
def expected_outcomes():
    """预期成果页"""
    from app.models.models import ExpectedOutcome
    outcomes = ExpectedOutcome.query.order_by(ExpectedOutcome.sort_order).all()
    return render_template('pages/project/expected_outcomes.html', outcomes=outcomes)
