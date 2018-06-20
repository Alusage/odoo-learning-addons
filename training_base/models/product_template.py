# Copyright 2018 Nicolas JEUDY
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = ['product.template']

    is_training = fields.Boolean(string='is training')
    certificate = fields.Text(string='Certificate', translate=True)
    goal = fields.Text(string='Goal', translate=True)
    description = fields.Text(string='Description', translate=True)
    content = fields.Text(string='Content', translate=True)
    methodology = fields.Text(string='Methodology', translate=True)
    validate = fields.Text(string='Validate', translate=True)
    public = fields.Text(string='Public', translate=True)
    prerequisite = fields.Text(string='Prerequisite', translate=True)
    our_value = fields.Text(string='Value', translate=True)

    contact_id = fields.Many2one('res.partner', string="Contact")
    domain_id = fields.Many2one('learning.domain', string="Domain")
    duration_info = fields.Char('Duration Info')
    price_info = fields.Char('Price info')
    duration_hour = fields.Float('Duration in hour(s)')

    subject_ids = fields.Many2many('learning.subject', string='Subject(s)')
