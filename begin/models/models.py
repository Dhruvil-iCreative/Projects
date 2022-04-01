# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def AddTag(self):
        # for rec in self:
        #     tag = self.env['res.partner.category'].search([("name", "=", "Best partner EVER")])
        #     if rec.customer_rank >= 5:
        #         rec.write({"category_id": [(4, tag)]})
        pass