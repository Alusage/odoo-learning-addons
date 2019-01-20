from odoo import models, fields


class LearningTeacher(models.Model):
    _inherit = 'learning.teacher'

    session_ids = fields.One2many('learning.timesession', 'teacher_id', 'Sessions')
