from odoo import models, fields


class LearningSubject(models.Model):
    _name = 'learning.subject'
    _rec_name = 'name'

    name = fields.Char('Name', required=True)
    code = fields.Char('Code')
    duration = fields.Float('Duration')
    description = fields.Html('Descrition')
    coeff = fields.Integer('Coeff')
    subject_type = fields.Many2one('learning.subject.type', string='Type')
    subject_theme = fields.Many2one('learning.subject.theme', string='Theme')
    product_id = fields.Many2one('product.template', string='Learning', domain=[('is_training', '=', True)])


class LearningSubjectType(models.Model):
    _name = 'learning.subject.type'

    name = fields.Char('Name')
    description = fields.Char('Description')
    sequence = fields.Integer('sequence', help="Sequence for the handle.", default=10)


class LearningSubjectTheme(models.Model):
    _name = 'learning.subject.theme'

    name = fields.Char('Name')
    sequence = fields.Integer('sequence', help="Sequence for the handle.", default=10)
