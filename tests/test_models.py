# -*- coding: utf-8 -*-
"""
单元测试模块
测试数据库模型、路由和视图功能
"""
import os
import sys
import unittest
import tempfile

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.models import (
    Project, LearningModule, Achievement, StudentProfile,
    VisitPlan, Motivation, ExpectedOutcome
)


class BaseModelTestCase(unittest.TestCase):
    """基础测试用例 - 设置测试应用和数据库"""

    def setUp(self):
        """每个测试前执行：创建测试应用和临时数据库"""
        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

    def tearDown(self):
        """每个测试后执行：清理数据库"""
        db.session.remove()
        db.drop_all()
        self.ctx.pop()


class ProjectModelTest(BaseModelTestCase):
    """项目模型测试"""

    def test_create_project(self):
        """测试创建项目"""
        project = Project(
            title='测试项目',
            subtitle='测试副标题',
            description='测试描述',
            category='main',
            status='进行中'
        )
        db.session.add(project)
        db.session.commit()

        self.assertIsNotNone(project.id)
        self.assertEqual(project.title, '测试项目')
        self.assertEqual(project.status, '进行中')

    def test_project_to_dict(self):
        """测试项目序列化"""
        from datetime import date
        project = Project(
            title='测试项目',
            start_date=date(2026, 7, 1),
            end_date=date(2026, 8, 31)
        )
        db.session.add(project)
        db.session.commit()

        data = project.to_dict()
        self.assertEqual(data['title'], '测试项目')
        self.assertEqual(data['start_date'], '2026-07-01')


class AchievementModelTest(BaseModelTestCase):
    """成果模型测试"""

    def test_create_achievement(self):
        """测试创建成果"""
        achievement = Achievement(
            title='测试竞赛',
            description='测试描述',
            category='竞赛',
            level='国家级',
            award='一等奖',
            is_featured=True
        )
        db.session.add(achievement)
        db.session.commit()

        self.assertIsNotNone(achievement.id)
        self.assertTrue(achievement.is_featured)
        self.assertEqual(achievement.level, '国家级')

    def test_achievement_to_dict(self):
        """测试成果序列化"""
        from datetime import date
        achievement = Achievement(
            title='测试专利',
            category='专利',
            level='国家级',
            date=date(2025, 1, 15)
        )
        db.session.add(achievement)
        db.session.commit()

        data = achievement.to_dict()
        self.assertEqual(data['category'], '专利')
        self.assertEqual(data['date'], '2025-01-15')


class StudentProfileModelTest(BaseModelTestCase):
    """学生档案模型测试"""

    def test_create_profile(self):
        """测试创建学生档案"""
        profile = StudentProfile(
            name='测试学生',
            major='机器人工程',
            political_status='共青团员',
            ranking='第1名/43人',
            skills='["ROS", "Python"]'
        )
        db.session.add(profile)
        db.session.commit()

        self.assertIsNotNone(profile.id)
        self.assertEqual(profile.name, '测试学生')
        self.assertEqual(profile.major, '机器人工程')


class LearningModuleModelTest(BaseModelTestCase):
    """学习模块模型测试"""

    def test_create_module(self):
        """测试创建学习模块"""
        project = Project(title='测试项目', category='main')
        db.session.add(project)
        db.session.flush()

        module = LearningModule(
            project_id=project.id,
            title='AI基础理论',
            sort_order=1,
            icon='fa-brain'
        )
        db.session.add(module)
        db.session.commit()

        self.assertIsNotNone(module.id)
        self.assertEqual(module.project_id, project.id)


class RouteTestCase(BaseModelTestCase):
    """路由测试"""

    def test_index_page(self):
        """测试首页访问"""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        """测试关于页面"""
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_contact_page(self):
        """测试联系页面"""
        response = self.client.get('/contact')
        self.assertEqual(response.status_code, 200)

    def test_project_list_page(self):
        """测试项目列表页"""
        response = self.client.get('/project/')
        self.assertEqual(response.status_code, 200)

    def test_learning_plan_page(self):
        """测试学习计划页"""
        response = self.client.get('/project/learning-plan')
        self.assertEqual(response.status_code, 200)

    def test_visit_plan_page(self):
        """测试参访计划页"""
        response = self.client.get('/project/visit-plan')
        self.assertEqual(response.status_code, 200)

    def test_motivation_page(self):
        """测试参与动机页"""
        response = self.client.get('/project/motivation')
        self.assertEqual(response.status_code, 200)

    def test_expected_outcomes_page(self):
        """测试预期成果页"""
        response = self.client.get('/project/expected-outcomes')
        self.assertEqual(response.status_code, 200)

    def test_achievement_list_page(self):
        """测试成果列表页"""
        response = self.client.get('/achievement/')
        self.assertEqual(response.status_code, 200)

    def test_achievement_list_with_filter(self):
        """测试成果筛选功能"""
        response = self.client.get('/achievement/?category=竞赛&level=国家级')
        self.assertEqual(response.status_code, 200)

    def test_profile_page(self):
        """测试个人档案页（无数据时返回404）"""
        response = self.client.get('/profile/')
        self.assertEqual(response.status_code, 404)

    def test_guide_index_page(self):
        """测试申请指南首页"""
        response = self.client.get('/guide/')
        self.assertEqual(response.status_code, 200)

    def test_guide_process_page(self):
        """测试申请流程页"""
        response = self.client.get('/guide/process')
        self.assertEqual(response.status_code, 200)

    def test_guide_materials_page(self):
        """测试申请材料页"""
        response = self.client.get('/guide/materials')
        self.assertEqual(response.status_code, 200)

    def test_guide_faq_page(self):
        """测试常见问题页"""
        response = self.client.get('/guide/faq')
        self.assertEqual(response.status_code, 200)

    def test_404_page(self):
        """测试404错误页"""
        response = self.client.get('/nonexistent-page')
        self.assertEqual(response.status_code, 404)


class DataIntegrityTest(BaseModelTestCase):
    """数据完整性测试"""

    def test_project_with_modules(self):
        """测试项目与学习模块的关联关系"""
        project = Project(title='测试项目', category='main')
        db.session.add(project)
        db.session.flush()

        module1 = LearningModule(project_id=project.id, title='模块1', sort_order=1)
        module2 = LearningModule(project_id=project.id, title='模块2', sort_order=2)
        db.session.add_all([module1, module2])
        db.session.commit()

        modules = project.learning_modules.order_by(LearningModule.sort_order).all()
        self.assertEqual(len(modules), 2)
        self.assertEqual(modules[0].title, '模块1')

    def test_achievement_filtering(self):
        """测试成果筛选"""
        achievements = [
            Achievement(title='国家级竞赛', category='竞赛', level='国家级'),
            Achievement(title='省级竞赛', category='竞赛', level='省级'),
            Achievement(title='专利', category='专利', level='国家级'),
        ]
        db.session.add_all(achievements)
        db.session.commit()

        national = Achievement.query.filter_by(level='国家级').all()
        self.assertEqual(len(national), 2)

        competitions = Achievement.query.filter_by(category='竞赛').all()
        self.assertEqual(len(competitions), 2)


if __name__ == '__main__':
    unittest.main()
