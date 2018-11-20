from odoo import api, models, _
from odoo.exceptions import UserError


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    cla_number = fields.Char('Cla number', readonly=True, states={'waiting_ufc': [('readonly', False), ]})
    state = fields.Selection([
        ('draft', 'Draft'),
        ('open', 'Open'),
        ('waiting_ufc', 'Waiting UFC'),
        ('in_payment', 'In Payment'),
        ('paid', 'Paid'),
        ('cancel', 'Cancelled'), ])

    @api.multi
    def invoice_waiting_ufc(self):
        return self.write({'state': 'waiting_ufc'})

    @api.multi
    def invoice_validate_ufc(self):
        return self.write({'state': 'open'})
