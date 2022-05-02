import datetime

from odoo import models, fields, api


class SaleOrderWiz(models.TransientModel):
    _name = 'sale.order.wiz'

    order_lines = fields.One2many('sale.order.line.wiz', 'product', string="Products")

    def sale_order_generation(self):
        order_lines = []
        for product in self.order_lines.product_id:
            order_lines.append((0, 0, {'product_id': product.id}))
        for i in self._context.get("active_ids"):
            self.env['sale.order'].create({
                'partner_id': i,
                'order_line': order_lines
            })
        return self.env['ir.actions.act_window']._for_xml_id("sale.action_quotations_with_onboarding")


class SaleOrderLine(models.TransientModel):
    _name = 'sale.order.line.wiz'

    product = fields.Many2one('sale.order.wiz')
    product_id = fields.Many2one('product.product', string="Products")
    quantity = fields.Float(default=1)
    unit_price = fields.Float(related="product_id.list_price")
