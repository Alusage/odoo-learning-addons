# Copyright 2018 Nicolas JEUDY
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Training Base',
    'summary': """
        Base module to add training management to odoo""",
    'version': '11.0.1.0.2',
    'license': 'AGPL-3',
    'author': 'Nicolas JEUDY, Odoo Community Association (OCA)',
    'website': 'https://www.pandachi.fr',
    'depends': [
        'base',
        'product',
        'event',
        'event_sale',
        'partner_firstname',
        'website_event_sale',
    ],
    'data': [
        'security/training_security.xml',
        'views/product_template.xml',
        'views/event_event.xml',
        'wizard/register_event.xml',
        'wizard/teacher_create_employee_wizard_view.xml',
        'wizard/event_registration_create_student.xml',
        'views/template.xml',
        'views/student.xml',
        'views/subject.xml',
        'views/teacher_view.xml',
    ],
    'demo': [
    ],
}
