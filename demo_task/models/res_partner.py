from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "res.partner"

    def create_partner(self):
        context = self._context
        self.env[context["active_model"]].create({"name": "ABC",
                                                  "company_type": "person",
                                                  "type": "contact"})

    def update_partner(self):
        self.write({
            'name': 'Dhruvil',
            'email': "modidhruvil42@gmail.com",
            'phone': '9638645033'
        })
