import logging
import re
import unicodedata

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])


def generate_login(first_name, family_name, login_exists_fn):
    def _sanitize(s):
        s = remove_accents(s).strip().lower()
        return re.sub(r'[^a-z]', '', s)
    first_name = _sanitize(first_name)
    family_name = _sanitize(family_name)
    candidate = ("%s%s" % (first_name[0], family_name))[0:8]
    i = 1
    while login_exists_fn(candidate):
        s = "%d" % i
        if len(candidate) > 8 - len(s):
            candidate = candidate[0:8-len(s)]
        candidate = candidate + s
        i += 1
    return candidate

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
    mothertongue_id = fields.Many2one('learning.lang', string="Langue maternelle")
    partner_id = fields.Many2one(
        'res.partner', 'Partner', required=True, ondelete="cascade")
    is_student = fields.Boolean(default=True)
    count_session = fields.Integer('Session', compute="_compute_session")
    course_detail_ids = fields.One2many('event.registration', 'student_id',
                                        'Course Details')
    cla_login = fields.Char('Login CLA', size=8)

    @api.model
    def create(self, values):
        record = super(LearningStudent, self).create(values) 
        _logger.debug("id: %s, lastname: %s, firstname: %s, cla_login: %s" % (record.id, record.lastname, record.firstname, record.cla_login))
        login_exists_fn = lambda login: len(self.env['learning.student'].search([('cla_login', '=', login)])) != 0
        if not values.get('cla_login', False) and not record['cla_login']:
            record['cla_login'] = generate_login(values.get('firstname'), values.get('lastname'), login_exists_fn)
        return record

    def _compute_session(self):
        for record in self:
            record.count_session = len(self.env['event.registration'].search([('student_id', '=', record.id)]).mapped('event_id'))

    @api.multi
    def action_view_session(self):
        session_ids = self.env['event.registration'].search([('student_id', '=', self.id)]).mapped('event_id')
        action = self.env.ref('training_base.ir_actions_act_window_session_r0').read()[0]
        if len(session_ids) > 1:
            action['domain'] = [('id', 'in', session_ids.ids)]
        elif len(session_ids) == 1:
            action['views'] = [(self.env.ref('event.view_event_form').id, 'form')]
            action['res_id'] = session_ids.ids[0]
        else:
            action = {'type': 'ir.actions.act_window_close'}
        return action
