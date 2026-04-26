# -*- coding: utf-8 -*-
"""
数据库初始化脚本
创建所有数据表并填充基于PPT内容的示例数据
"""
import os
import sys
from datetime import date

# 添加项目根目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app, db
from app.models.models import (
    Project, LearningModule, Achievement, StudentProfile,
    VisitPlan, Motivation, ExpectedOutcome
)


def init_db():
    """初始化数据库"""
    app = create_app('development')

    with app.app_context():
        # 创建所有表
        db.create_all()
        print("✓ 数据表创建成功")

        # 检查是否已有数据
        if Project.query.first():
            print("⚠ 数据库已有数据，跳过初始化数据填充")
            return

        # 填充示例数据
        seed_data()
        print("✓ 示例数据填充完成")


def seed_data():
    """填充基于PPT内容的示例数据"""

    # ========== 项目信息 ==========
    project = Project(
        title='粤港澳大湾区人工智能与跨学科创新实践访学项目',
        subtitle='人工智能与跨学科应用（科技创新与社会实践）',
        description='本项目由兰州城市学院重点扶持，旨在通过赴粤港澳大湾区开展人工智能与跨学科创新实践访学，'
                    '深入学习AI基础理论、前沿技术实操，参访头部企业与高校，全面提升学生的学术视野、'
                    '技术能力和创新思维。',
        category='main',
        status='进行中',
        start_date=date(2026, 7, 1),
        end_date=date(2026, 8, 31),
    )
    db.session.add(project)
    db.session.flush()  # 获取project.id

    # ========== 学习模块 ==========
    modules_data = [
        {
            'title': '人工智能基础理论',
            'subtitle': 'AI全域筑基 · 算法补阙',
            'description': '系统学习人工智能基础理论，掌握机器学习核心算法，夯实AI理论基础',
            'tech_content': '掌握Transformer架构、深度学习与神经网络基础、机器学习实践',
            'practice_direction': '路径规划算法应用、掌握AI工具编程落地实操',
            'ability_improvement': '夯实AI理论基础',
            'sort_order': 1,
            'icon': 'fa-brain',
        },
        {
            'title': '前沿技术实操训练',
            'subtitle': 'AI全域筑基 · 素材设计',
            'description': '实战OpenCV和YOLO视觉引导，掌握计算机视觉和自然语言处理在工业场景的前沿应用',
            'tech_content': '实战OpenCV和YOLO视觉引导、计算机视觉与NLP工业应用',
            'practice_direction': '工业机器人视觉引导',
            'ability_improvement': '掌握AI工具编程落地实操',
            'sort_order': 2,
            'icon': 'fa-robot',
        },
        {
            'title': '产业参观与案例研讨',
            'subtitle': '一线实操练 · 行业视野与思维拓展',
            'description': '研学头部企业大模型落地，参与企业参访和项目开发，高校前沿AI技术学习',
            'tech_content': '研学头部企业大模型落地、高校前沿AI技术',
            'practice_direction': 'AI+医疗、AI+制造等行业全流程项目案例分析',
            'ability_improvement': '拓宽学术产业视野，提升团队协作与问题解决能力',
            'sort_order': 3,
            'icon': 'fa-building',
        },
        {
            'title': '成果转化与能力提升',
            'subtitle': '对标顶尖势 · 产研深耕 · 学以致用',
            'description': '案例库搭建、项目开发能力提升，完成机器人智能项目开发和语音控制落地',
            'tech_content': '案例库搭建、项目开发、机器人智能项目开发',
            'practice_direction': '完成机器人语音控制落地、准备返校后的分享会内容',
            'ability_improvement': '具备完整项目全流程开发能力',
            'sort_order': 4,
            'icon': 'fa-lightbulb',
        },
    ]

    for m in modules_data:
        module = LearningModule(project_id=project.id, **m)
        db.session.add(module)

    # ========== 学生档案 ==========
    profile = StudentProfile(
        name='田硕',
        major='机器人工程',
        political_status='共青团员',
        ranking='第1名/43人',
        gpa='班级前列',
        skills='["ROS", "Unity3D", "SolidWorks", "Python", "OpenCV", "YOLO", "深度学习", "机器学习", '
               '"机器人运动学建模", "路径规划", "传感器融合", "数字孪生", "电子控制", "计算机算法"]',
        research_interests='机器人与人工智能交叉领域、智能控制、数字孪生应用、跨学科建模、数据驱动分析',
        awards_summary='国家级竞赛获奖3项，省级竞赛获奖14项，校级获奖22项。连续两年荣获校级"科技创新奖"'
                       '及"学校奖学金一等奖"。曾获睿抗机器人开发者大赛国家一等奖等十余项AI类竞赛奖项。',
        bio='专注机器人与人工智能交叉领域，具备机器人工程与AI交叉领域的扎实知识储备。'
            '掌握了环境感知、自主导航等核心技术。作为项目核心骨干，统筹大创项目全周期管理，'
            '涵盖需求分析、方案设计、代码迭代与测试验证。在实践中深度融合电子控制与计算机算法，'
            '形成"理论-仿真-实物-优化"的标准工程实践范式。',
    )
    db.session.add(profile)

    # ========== 成果展示 ==========
    achievements_data = [
        # 国家级竞赛
        {'title': '睿抗机器人开发者大赛', 'description': '在睿抗机器人开发者大赛中荣获国家一等奖，展示出色的机器人开发能力', 'category': '竞赛', 'level': '国家级', 'award': '国家一等奖', 'date': date(2025, 6, 1), 'is_featured': True},
        {'title': '全国大学生机器人大赛', 'description': '参加全国大学生机器人大赛，展现扎实的机器人系统开发能力', 'category': '竞赛', 'level': '国家级', 'award': '国家级奖项', 'date': date(2025, 5, 1), 'is_featured': True},
        {'title': '全国大学生创新创业大赛', 'description': '在全国大学生创新创业大赛中获得优异成绩', 'category': '竞赛', 'level': '国家级', 'award': '国家级奖项', 'date': date(2024, 10, 1), 'is_featured': False},
        # 省级竞赛
        {'title': '工业协作机器人专项赛', 'description': '熟练运用ROS、Unity3D、SolidWorks完成机器人运动学建模、路径规划与传感器融合，获省级一等奖', 'category': '竞赛', 'level': '省级', 'award': '省级一等奖', 'date': date(2025, 4, 1), 'is_featured': True},
        {'title': '省级机器人竞赛', 'description': '在省级机器人竞赛中获得优异成绩', 'category': '竞赛', 'level': '省级', 'award': '省级奖项', 'date': date(2024, 11, 1), 'is_featured': False},
        {'title': '省级AI创新应用大赛', 'description': '展示AI技术在机器人领域的创新应用', 'category': '竞赛', 'level': '省级', 'award': '省级奖项', 'date': date(2024, 9, 1), 'is_featured': False},
        # 专利软著
        {'title': '可多角度旋转折叠式摄像头', 'description': '已获授权实用新型专利，创新设计了可多角度旋转折叠的摄像装置', 'category': '专利', 'level': '国家级', 'award': '实用新型专利（已授权）', 'date': date(2025, 1, 15), 'is_featured': True},
        {'title': '天枢矩阵低空管控系统', 'description': '登记计算机软件著作权，实现了低空经济领域的智能管控系统', 'category': '软著', 'level': '国家级', 'award': '计算机软件著作权（已登记）', 'date': date(2025, 3, 1), 'is_featured': True},
        # 科研项目
        {'title': '大学生创新创业训练计划项目', 'description': '作为项目核心骨干，聚焦低空经济与智能机器人交叉领域，从理论到实物形成完整闭环，技术成果具备明确的产业落地场景与跨学科应用价值', 'category': '项目', 'level': '校级', 'award': '核心骨干', 'date': date(2024, 6, 1), 'is_featured': True},
        # 校级荣誉
        {'title': '校级科技创新奖', 'description': '连续两年荣获校级"科技创新奖"，表彰在科技创新方面的突出表现', 'category': '荣誉', 'level': '校级', 'award': '科技创新奖', 'date': date(2025, 1, 1), 'is_featured': False},
        {'title': '学校奖学金一等奖', 'description': '连续两年荣获学校奖学金一等奖，学业成绩优异', 'category': '荣誉', 'level': '校级', 'award': '一等奖学金', 'date': date(2025, 1, 1), 'is_featured': False},
    ]

    for a in achievements_data:
        achievement = Achievement(**a)
        db.session.add(achievement)

    # ========== 参访计划 ==========
    visits_data = [
        {'title': '数字孪生基础平台实训', 'location': '粤港澳大湾区', 'description': '学习数字孪生技术基础，了解平台架构与应用场景', 'visit_type': '企业', 'sort_order': 1, 'icon': 'fa-cube'},
        {'title': '装备制造场景应用实践', 'location': '粤港澳大湾区', 'description': '深入装备制造企业，了解AI技术在智能制造中的实际应用', 'visit_type': '企业', 'sort_order': 2, 'icon': 'fa-industry'},
        {'title': '物联网与AI研发中心', 'location': '粤港澳大湾区', 'description': '参访物联网与AI研发中心，了解前沿技术发展趋势', 'visit_type': '企业', 'sort_order': 3, 'icon': 'fa-wifi'},
        {'title': '系统集成与制造', 'location': '粤港澳大湾区', 'description': '学习系统集成技术在制造业中的应用', 'visit_type': '企业', 'sort_order': 4, 'icon': 'fa-cogs'},
        {'title': '知识产权与科技服务', 'location': '粤港澳大湾区', 'description': '了解知识产权保护与科技服务体系', 'visit_type': '机构', 'sort_order': 5, 'icon': 'fa-certificate'},
        {'title': '设计与3D打印', 'location': '粤港澳大湾区', 'description': '学习工业设计与3D打印技术在产品开发中的应用', 'visit_type': '企业', 'sort_order': 6, 'icon': 'fa-print'},
    ]

    for v in visits_data:
        visit = VisitPlan(**v)
        db.session.add(visit)

    # ========== 参与动机 ==========
    motivations_data = [
        {'title': '专业进阶与技术渴求', 'subtitle': '算法能力补强 · 理论体系重构', 'description': '作为机器人工程专业的学生，在校内已掌握了扎实的机械控制与基础编程能力，希望通过访学补齐深度学习和神经网络等AI算法短板', 'keywords': '深度学习,神经网络,AI算法', 'sort_order': 1, 'icon': 'fa-graduation-cap'},
        {'title': '智能控制升级', 'subtitle': '智能控制升级 · 工科拓边界', 'description': '将AI技术与机器人智能控制深度融合，拓展工科边界', 'keywords': '智能控制,机器人,AI融合', 'sort_order': 2, 'icon': 'fa-microchip'},
        {'title': '地域优势与产业洞察', 'subtitle': '产业前沿对标 · 创新生态体验', 'description': '粤港澳大湾区是全球人工智能与智能制造的产业高地。走进大湾区产业高地亲身感受AI落地逻辑', 'keywords': '大湾区,产业高地,AI落地', 'sort_order': 3, 'icon': 'fa-map-marker-alt'},
        {'title': '职业视野开拓', 'subtitle': '跳出闭门造车 · 职业视野开拓', 'description': '参访顶尖企业，了解AI行业最新发展趋势和人才需求', 'keywords': '职业规划,企业参访,行业趋势', 'sort_order': 4, 'icon': 'fa-briefcase'},
        {'title': '知行合一与回馈建设', 'subtitle': '经验成果转化 · 朋辈示范引领', 'description': '不仅是一名学习者，更是一名传播者。要把前沿经验带回学校，带动身边同学共同关注人工智能', 'keywords': '知识传播,朋辈引领,回馈', 'sort_order': 5, 'icon': 'fa-hands-helping'},
        {'title': '聚力东西科创', 'subtitle': '服务区域发展 · 聚力东西科创', 'description': '将前沿经验带回学校，服务区域发展，聚力东西科创合作', 'keywords': '区域发展,科创合作,东西部', 'sort_order': 6, 'icon': 'fa-globe-asia'},
    ]

    for m in motivations_data:
        motivation = Motivation(**m)
        db.session.add(motivation)

    # ========== 预期成果 ==========
    outcomes_data = [
        {'title': '技术能力提升', 'description': '掌握大湾区前沿的AI跨学科应用技术，掌握机器视觉与智能控制等前沿技术，将AI技术与传统行业结合，探索数字化转型方案', 'category': '学术', 'sort_order': 1, 'icon': 'fa-chart-line'},
        {'title': '学术成果转化', 'description': '尝试撰写并投稿1篇相关领域的会议论文或申请1项实用新型专利及软著，争取发表论文或申请专利，将所学用于学科竞赛', 'category': '学术', 'sort_order': 2, 'icon': 'fa-file-alt'},
        {'title': '产业应用落地', 'description': '基于访学期间研发的"AI+机器人"跨学科解决方案，将访学成果中的路径规划算法应用于其工业机器人升级项目，推动技术从实验室走向产线', 'category': '产业', 'sort_order': 3, 'icon': 'fa-rocket'},
        {'title': '创新模式构建', 'description': '依托访学项目构建的"AI+智能制造"创新模型，助力智能制造数字化转型，形成可复制的"高校研发-企业落地"成果转化模式', 'category': '产业', 'sort_order': 4, 'icon': 'fa-project-diagram'},
        {'title': '青年创新联盟', 'description': '通过访学积累的跨学科创新经验，计划联合访学期间结识的团队与内地企业，共同发起"AI+X"青年创新联盟，推动技术、人才、资本的多方联动', 'category': '社会', 'sort_order': 5, 'icon': 'fa-users'},
    ]

    for o in outcomes_data:
        outcome = ExpectedOutcome(**o)
        db.session.add(outcome)

    db.session.commit()


if __name__ == '__main__':
    init_db()
