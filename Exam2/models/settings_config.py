from ast import literal_eval
from datetime import date, datetime
from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_Exam2 = fields.Boolean("Install Contacts")
    sale_order_ids = fields.Many2many('sale.order', string="Sale Order", required=False,
                                      domain=[("date_order", '>=', datetime(date.today().year, date.today().month, 1)),
                                              ("date_order", '<', datetime(date.today().year, date.today().month+1, 1))])

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        irvalues = self.env['ir.config_parameter']
        module_exam2 = irvalues.get_param('Exam2.module_Exam2')
        sale_order_ids = irvalues.get_param('Exam2.sale_order_ids')
        lines = False
        if sale_order_ids:
            lines = [(6, 0, literal_eval(sale_order_ids))]
        return {
            'module_Exam2': module_exam2,
            'sale_order_ids': lines,
        }

    @api.model
    def set_values(self):
        res = super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].set_param(
            'Exam2.module_Exam2', self.module_Exam2)
        self.env['ir.config_parameter'].set_param(
            'Exam2.sale_order_ids', self.sale_order_ids.ids)
        return res
