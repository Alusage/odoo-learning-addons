# Copyright 2018 Nicolas JEUDY
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
import barcode
from barcode.writer import ImageWriter
import base64
import logging
from io import BytesIO
import re
import unicodedata

from odoo import api, fields, models, _

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


class ResPartner(models.Model):
    _inherit = 'res.partner'

    student_barcode = fields.Binary('Barcode', attachment=True, compute="_compute_barcode", store=True)

    is_student = fields.Boolean("Is student ?")
    birth_date = fields.Date('Birth Date', required=False)
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], 'Gender', required=False)
    nationality = fields.Many2one('res.country', 'Nationality')
    visa_info = fields.Char('Visa Info', size=64)
    id_number = fields.Char('ID Card Number', size=64)
    mothertongue_id = fields.Many2one('learning.lang', string="Langue maternelle")
    cla_login = fields.Char('Login CLA', size=8)

    @api.depends('ref')
    def _compute_barcode(self):
        for record in self:
            if record.ref:
                CODE39 = barcode.get_barcode_class('code39')
                code39 = CODE39(record.ref, writer=ImageWriter(), add_checksum=False)
                fp = BytesIO()
                code39.write(fp)
                #barcode.generate('code39', self.ref, writer=ImageWriter(), output=fp)
                record.student_barcode = base64.b64encode(fp.getvalue())
            else:
                record.student_barcode = False


    @api.multi
    @api.constrains('birth_date')
    def _check_birthdate(self):
        for record in self:
            if record.birth_date and record.birth_date > fields.Date.today():
                raise ValidationError(_(
                    "Birth Date can't be greater than current date!"))
