from odoo import models, fields, api


class AddProductWiz(models.TransientModel):
    _name = 'products.add'

    product_ids = fields.Many2many(comodel_name="product.product", string="Products")

    @api.model
    def create(self, vals):
        res = super(AddProductWiz, self).create(vals)
        a = self.env[self.env.context.get('active_model')].browse(self.env.context.get('active_id'))
        for i in res.product_ids:
            a.write({
                'order_line': [(0, 0, {'product_id': i.id})]
            })
        return res
