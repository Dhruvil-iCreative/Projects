from odoo import models, fields


class UpdateProduct(models.Model):
    _inherit = 'product.template'

    is_rental = fields.Boolean("Is Rental?")
    rental_type_id = fields.Many2one(comodel_name="rental.type", string="Rental Type")
