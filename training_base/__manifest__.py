# Copyright 2018 Nicolas JEUDY
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

{
    'name': 'Training Base',
    'summary': """
        Base module to add training management to odoo""",
    'version': '11.0.1.0.0',
    'license': 'AGPL-3',
    'author': 'Nicolas JEUDY, Odoo Community Association (OCA)',
    'website': 'https://www.pandachi.fr',
    'depends': [
        'base',
        'product',
        'event',
        'event_sale',
        'partner_firstname',
    ],
    'data': [
        'views/product_template.xml',
        'views/event_event.xml',
    ],
    'demo': [
    ],
}
