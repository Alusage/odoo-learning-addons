import logging
from odoo import api, models, _
from odoo.exceptions import UserError

_logger = logging.getLogger(__name__)


class SaleOrder(models.Model):
    _inherit = "sale.order"

    @api.multi
    def action_quotation_send(self):
        '''
        This function opens a window to compose an email, with the edi sale template message loaded by default
        '''
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        res = super(SaleOrder,self).action_quotation_send()
        if self.x_project_mode:
            res['context']['mark_so_as_sent'] = False
        return res

    @api.multi
    def _cart_update(self, product_id=None, line_id=None, add_qty=0, set_qty=0, **kwargs):
        if add_qty:
            add_qty = int(add_qty)
        if set_qty:
            set_qty = int(set_qty)
        return super(SaleOrder, self)._cart_update(product_id=product_id,
                                                   line_id=line_id,
                                                   add_qty=add_qty,
                                                   set_qty=set_qty,
                                                   **kwargs)
