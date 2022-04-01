# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    mobile = fields.Char()
    email = fields.Char()
    uids = fields.Many2one("begin.begin")

    @api.onchange("partner_id")
    def _onchange_partner_id(self):
        for rec in self:
            rec.mobile = rec.partner_id.phone
            rec.email = rec.partner_id.email

    @api.constrains('payment_term_id', 'partner_id')
    def _check_payment_term(self):
        for rec in self:
            if rec.payment_term_id.name != rec.partner_id.property_supplier_payment_term_id.name:
                raise UserError('Payment Terms do not match!')

    def default_wiz(self):
        return self.env['ir.actions.act_window']._for_xml_id("begin.sale_order_default_wiz_views_action_window")

    def get_values(self):
        res = self.env['res.partner'].search([("email", '!=', False)]).read(['name', 'email'])
        res1 = self.env['res.partner'].browse([3, 15]).read(['name'])
        res2 = self.env['res.partner'].search_read([("email", "!=", False)], fields=['name', 'email'])
        res3 = self.env['sale.order'].browse([self.env.context.get('active_id')]).read(['name'])
        print(res, "****************************************")
        print(res1, "############@########################################")
        print(res2, "$$$$$$$$$$$$$$$$$$$$$$$$$%$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print(res3, "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        return res, res1, res2, res3

    def action_confirm(self):
        count = 0
        for rec in self:
            count = len(rec.order_line)
        print(count, "#####################################################")

        if count <= 3:
            return super(SaleOrder, self).action_confirm()
        else:
            raise UserError('You can only add max 3 lines per order.')

    @api.model
    def create(self, vals):
        res = super(SaleOrder, self).create(vals)
        if res.partner_id.customer_rank > 5:
            best_categ_id = self.env.ref("begin.res_partner_category_best_customer").id
            res.partner_id.write({'category_id': [(4, best_categ_id)]})
        return res
