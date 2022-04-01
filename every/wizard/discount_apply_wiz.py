from odoo import models,api,fields

class DiscountApplyWiz(models.TransientModel):
    _name = "discount.apply.wiz"

    discount=fields.Float(string="Discount")

    def apply_discount(self):
        print("yeah clicked perfectly!")