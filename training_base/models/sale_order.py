from odoo import api, models, _
from odoo.exceptions import UserError


class SaleOrder(models.Model):
    _inherit = "sale.order"

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
