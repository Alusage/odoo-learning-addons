# Copyright 2018 Nicolas JEUDY
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class EventEvent(models.Model):
    _inherit = ['event.event']

    duration_week = fields.Integer('Duration in week(s)')
    duration_hour = fields.Float('Duration in hour(s)')
