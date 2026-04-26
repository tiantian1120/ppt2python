# -*- coding: utf-8 -*-
"""
数据库模型模块
定义所有数据表结构
"""
from datetime import datetime
from app import db


class Project(db.Model):
    """项目信息表"""
    __tablename__ = 'projects'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, comment='项目标题')
    subtitle = db.Column(db.String(300), comment='项目副标题')
    description = db.Column(db.Text, comment='项目描述')
    category = db.Column(db.String(50), comment='项目类别')
    status = db.Column(db.String(20), default='进行中', comment='项目状态')
    start_date = db.Column(db.Date, comment='开始日期')
    end_date = db.Column(db.Date, comment='结束日期')
    cover_image = db.Column(db.String(200), comment='封面图片路径')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # 关系
    learning_modules = db.relationship('LearningModule', backref='project', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'description': self.description,
            'category': self.category,
            'status': self.status,
            'start_date': self.start_date.strftime('%Y-%m-%d') if self.start_date else '',
            'end_date': self.end_date.strftime('%Y-%m-%d') if self.end_date else '',
            'cover_image': self.cover_image,
        }


class LearningModule(db.Model):
    """学习模块表"""
    __tablename__ = 'learning_modules'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False, comment='模块标题')
    subtitle = db.Column(db.String(300), comment='模块副标题')
    description = db.Column(db.Text, comment='模块描述')
    tech_content = db.Column(db.Text, comment='技术学习内容')
    practice_direction = db.Column(db.Text, comment='实践应用方向')
    ability_improvement = db.Column(db.Text, comment='综合能力提升')
    sort_order = db.Column(db.Integer, default=0, comment='排序')
    icon = db.Column(db.String(100), comment='图标标识')
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'project_id': self.project_id,
            'title': self.title,
            'subtitle': self.subtitle,
            'description': self.description,
            'tech_content': self.tech_content,
            'practice_direction': self.practice_direction,
            'ability_improvement': self.ability_improvement,
            'sort_order': self.sort_order,
            'icon': self.icon,
        }


class Achievement(db.Model):
    """成果展示表"""
    __tablename__ = 'achievements'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, comment='成果标题')
    description = db.Column(db.Text, comment='成果描述')
    category = db.Column(db.String(50), comment='成果类别：竞赛/专利/软著/论文/项目')
    level = db.Column(db.String(50), comment='级别：国家级/省级/校级')
    award = db.Column(db.String(200), comment='奖项/荣誉')
    date = db.Column(db.Date, comment='获得日期')
    image = db.Column(db.String(200), comment='成果图片')
    is_featured = db.Column(db.Boolean, default=False, comment='是否精选展示')
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'level': self.level,
            'award': self.award,
            'date': self.date.strftime('%Y-%m-%d') if self.date else '',
            'image': self.image,
            'is_featured': self.is_featured,
        }


class StudentProfile(db.Model):
    """学生档案表"""
    __tablename__ = 'student_profiles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, comment='姓名')
    major = db.Column(db.String(100), comment='专业')
    political_status = db.Column(db.String(50), comment='政治面貌')
    ranking = db.Column(db.String(50), comment='综合测评排名')
    gpa = db.Column(db.String(20), comment='GPA/成绩')
    skills = db.Column(db.Text, comment='技能列表(JSON)')
    research_interests = db.Column(db.Text, comment='研究方向')
    awards_summary = db.Column(db.Text, comment='获奖概要')
    bio = db.Column(db.Text, comment='个人简介')
    avatar = db.Column(db.String(200), comment='头像路径')
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'major': self.major,
            'political_status': self.political_status,
            'ranking': self.ranking,
            'gpa': self.gpa,
            'skills': self.skills,
            'research_interests': self.research_interests,
            'awards_summary': self.awards_summary,
            'bio': self.bio,
            'avatar': self.avatar,
        }


class VisitPlan(db.Model):
    """参访计划表"""
    __tablename__ = 'visit_plans'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, comment='参访标题')
    location = db.Column(db.String(200), comment='参访地点')
    description = db.Column(db.Text, comment='参访描述')
    visit_type = db.Column(db.String(50), comment='参访类型：企业/高校/实验室')
    sort_order = db.Column(db.Integer, default=0, comment='排序')
    icon = db.Column(db.String(100), comment='图标标识')
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'location': self.location,
            'description': self.description,
            'visit_type': self.visit_type,
            'sort_order': self.sort_order,
            'icon': self.icon,
        }


class Motivation(db.Model):
    """参与动机表"""
    __tablename__ = 'motivations'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, comment='动机标题')
    subtitle = db.Column(db.String(200), comment='副标题')
    description = db.Column(db.Text, comment='动机描述')
    keywords = db.Column(db.String(200), comment='关键词')
    sort_order = db.Column(db.Integer, default=0, comment='排序')
    icon = db.Column(db.String(100), comment='图标标识')
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'subtitle': self.subtitle,
            'description': self.description,
            'keywords': self.keywords,
            'sort_order': self.sort_order,
            'icon': self.icon,
        }


class ExpectedOutcome(db.Model):
    """预期成果表"""
    __tablename__ = 'expected_outcomes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, comment='成果标题')
    description = db.Column(db.Text, comment='成果描述')
    category = db.Column(db.String(50), comment='类别：学术/产业/社会')
    sort_order = db.Column(db.Integer, default=0, comment='排序')
    icon = db.Column(db.String(100), comment='图标标识')
    created_at = db.Column(db.DateTime, default=datetime.now)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'sort_order': self.sort_order,
            'icon': self.icon,
        }
