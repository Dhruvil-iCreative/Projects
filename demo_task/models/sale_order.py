from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = "sale.order"

    def cron_demo_method(self):
        self.search([("state", "=", "done")]).write({
            'state': 'draft'
        })
