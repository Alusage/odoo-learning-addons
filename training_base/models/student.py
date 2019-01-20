from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LearningStudent(models.Model):
    _name = 'learning.student'
    _inherits = {'res.partner': 'partner_id'}

    # blood_group = fields.Selection(
    #     [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
    #      ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
    #     'Blood Group')
    # gender = fields.Selection(
    #     [('m', 'Male'), ('f', 'Female'),
    #      ('o', 'Other')], 'Gender')
    birth_date = fields.Date('Birth Date', required=False)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], 'Gender', required=False)
    nationality = fields.Many2one('res.country', 'Nationality')
    visa_info = fields.Char('Visa Info', size=64)
    id_number = fields.Char('ID Card Number', size=64)
    already_partner = fields.Boolean('Already Partner')
    partner_id = fields.Many2one(
        'res.partner', 'Partner', required=True, ondelete="cascade")
    is_student = fields.Boolean(default=True)
    course_detail_ids = fields.One2many('event.registration', 'student_id',
                                        'Course Details')
