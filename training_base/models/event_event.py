# Copyright 2018 Nicolas JEUDY
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class EventEvent(models.Model):
    _inherit = ['event.event']

    duration_week = fields.Integer('Duration in week(s)')
    duration_hour = fields.Float('Duration in hour(s)')
    training_id = fields.Many2one('product.template', string='Training', domain=[('is_training', '=', True)])


class EventRegistration(models.Model):
    _inherit = 'event.registration'

    student_id = fields.Many2one('learning.student', string="Student")

    @api.multi
    def confirm_registration(self):
        self.ensure_one()
        self.state = 'open'
        _logger.debug("##### ICI ?")
        _logger.debug("##### ICI - %s " % self.event_ticket_id.filtered(lambda line: line.product_id.is_training))
        res = super(EventRegistration, self).confirm_registration()

        # auto-trigger after_sub (on subscribe) mail schedulers, if needed
        if any(self.event_ticket_id.filtered(lambda line: line.product_id.is_training)):
            return self.env['ir.actions.act_window'].with_context(default_event_registration_id=self.id).for_xml_id('training_base', 'action_event_registration_create_student')
        _logger.debug("##### ICI 2 ?")
        return res
