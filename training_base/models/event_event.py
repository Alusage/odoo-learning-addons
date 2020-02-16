# Copyright 2018 Nicolas JEUDY
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import logging
import datetime
from odoo import api, fields, models, _

_logger = logging.getLogger(__name__)


class EventEvent(models.Model):
    _inherit = ['event.event']

    duration_week = fields.Integer('Duration in week(s)')
    duration_hour = fields.Float('Duration in hour(s)')
    date_examen = fields.Date('Date examen')
    training_id = fields.Many2one('product.template', string='Training', domain=[('is_training', '=', True)])
    datefinj_2 = fields.Date(compute='_compute_date_format', string="Date j-2")
    datefinj_2_format = fields.Char(compute='_compute_date_format', string="Date j-2 format")
    date_begin_format = fields.Char(compute='_compute_date_format', string="Date debut format")
    date_end_format = fields.Char(compute='_compute_date_format', string="Date fin format")
    batch_ids = fields.One2many('learning.batch', 'course_id', 'Groupe(s)')

    @api.depends('date_end', 'date_begin')
    def _compute_date_format(self):
        for rec in self:
            if rec.date_end:
                datefinj_2 = rec.date_end - datetime.timedelta(days=2)
                rec.datefinj_2 = datefinj_2.date()
                rec.datefinj_2_format = rec.datefinj_2.strftime('%d/%m/%Y')

                rec.date_end_format = rec.date_end.strftime('%Y-%m-%d')
            if rec.date_begin:
                rec.date_begin_format = rec.date_begin.strftime('%Y-%m-%d')

class EventRegistration(models.Model):
    _inherit = 'event.registration'

    is_training = fields.Boolean(related='event_id.training_id.is_training', readonly="1", store=True)
    student_id = fields.Many2one('learning.student', string="Student")
    current_level = fields.Many2one('learning.level', string="Current Level")
    prepared_level = fields.Many2one('learning.level', string="Prepared Level")
    batch_id = fields.Many2one(
        'learning.batch', 'Group', domain="[('course_id', '=', event_id)]")

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
