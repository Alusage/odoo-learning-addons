{
    'name': 'Training Attendance',
    'version': '12.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Attendances',
    'complexity': "easy",
    'author': 'Myceliandre',
    'website': 'http://www.myceliandre.fr',
    'depends': ['training_timetable'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'wizards/attendance_import_view.xml',
        'wizards/student_attendance_wizard_view.xml',
        'views/attendance_register_view.xml',
        'views/attendance_sheet_view.xml',
        'views/attendance_line_view.xml',
        'report/student_attendance_report.xml',
        'report/report_menu.xml',
        'menus/menu.xml'
    ],
    'test': [
        # 'test/res_users_test.yml',
        # 'test/attendance_sub_value_test.yml',
        # 'test/attendance_process_test.yml'
    ],
    'demo': [
        # 'demo/attendance_register_demo.xml',
        # 'demo/attendance_sheet_demo.xml',
        # 'demo/attendance_line_demo.xml',
    ],
    'images': [
        'static/description/openeducat_attendance_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
