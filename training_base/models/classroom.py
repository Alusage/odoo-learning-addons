from odoo import models, fields, api


class LearningClassroom(models.Model):
    _name = "learning.classroom"
    _description = "Classroom"

    name = fields.Char('Name', size=16, required=True)
    code = fields.Char('Code', size=16, required=True)
    capacity = fields.Integer(string='No of Person')

    _sql_constraints = [
        ('unique_classroom_code',
         'unique(code)', 'Code should be unique per classroom!')]
