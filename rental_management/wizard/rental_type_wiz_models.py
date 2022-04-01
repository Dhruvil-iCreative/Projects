from odoo import models, fields, api


class RentalTypeWiz(models.TransientModel):
    _name = "rental.type.wiz"
    # _inherit = "rental.type"
    _description = 'rental.type.wiz'

    name = fields.Char(required=True)
    code = fields.Integer()
    description = fields.Text()

    def create_rec(self):
        # rtn = super(RentalType, self).create(vals)
        context = self._context
        self.env[context["active_model"]].create({"name": self.name})

    def update_rec(self):
        print(self)
        context = self._context
        rental_type = self.env[context["active_model"]].browse(context["active_id"])
        rental_type.write({"name": self.name})
