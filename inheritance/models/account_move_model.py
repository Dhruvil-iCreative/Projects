from odoo import models, fields, api
from odoo.exceptions import UserError


class AccountMove(models.Model):
    _inherit = ["account.move"]

    @api.model
    def create_invoices(self):
        vendor_ids = self.invoice_line_ids.mapped("vendor_id.id")
        if vendor_ids:
            for vendor_id in vendor_ids:
                a = []
                for line in self.invoice_line_ids.filtered(lambda x: x.vendor_id.id == vendor_id):
                    a.append((0, 0, {"product_id": line.product_id.id, "price_unit": line.vendor_price}))
                res = self.create({
                    'move_type': 'in_invoice',
                    'partner_id': vendor_id,
                    'invoice_line_ids': a
                })
        return self.env['ir.actions.act_window']._for_xml_id("account.action_move_in_invoice_type")
