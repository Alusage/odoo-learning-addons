{
    'name': 'Training Timetable',
    'version': '12.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage TimeTables',
    'complexity': "easy",
    'author': 'Myceliandre',
    'website': 'http://www.myceliandre.fr',
    'depends': ['training_base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/timetable_view.xml',
        'views/timing_view.xml',
        'views/teacher_view.xml',
        'report/report_timetable_student_generate.xml',
        'report/report_timetable_teacher_generate.xml',
        'report/report_menu.xml',
        'wizard/generate_timetable_view.xml',
        'wizard/time_table_report.xml',
        'wizard/session_confirmation.xml',
        'views/timetable_templates.xml',
        'menus/menu.xml',
    ],
    'demo': [
        # 'demo/timing_demo.xml',
        # 'demo/op_timetable_demo.xml'
    ],
    'test': [
        # 'test/timetable_sub_value.yml',
        # 'test/generate_timetable.yml'
    ],
    'images': [
        'static/description/openeducat_timetable_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
