from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LearningDomain(models.Model):
    _name = 'learning.domain'

    name = fields.Char('Name')
    code = fields.Char('Code', translate=False)
