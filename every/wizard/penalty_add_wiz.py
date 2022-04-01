from odoo import models,api,fields

class DiscountApplyWiz(models.TransientModel):
    _name = "penalty.add.wiz"

    penalty=fields.Float(string="Penalty")

    def add_penalty(self):
        print("Penalty applied successfully!!!!")
