from odoo import models, fields, api


class AccountMoveLine(models.Model):
    _inherit = ["account.move.line"]

    delivery_address = fields.Many2one('res.partner', string="Delivery Address")
    vendor_id = fields.Many2one('res.partner', string="Vendor")
    vendor_price = fields.Float(string="Vendor Price")
    planned_gp = fields.Float(string="Planned GP%")
    description = fields.Text(compute="compute_description")

    @api.onchange('vendor_price', 'price_unit')
    def onchange_price_gp(self):
        for rec in self:
            if rec.price_unit:
                rec.planned_gp = ((rec.price_unit-rec.vendor_price)/rec.price_unit)*100
            else:
                rec.planned_gp = 0

    @api.depends('delivery_address', 'product_id')
    def compute_description(self):
        for rec in self:
            rec.description = f'{rec.product_id.name}-{rec.delivery_address.city}'
