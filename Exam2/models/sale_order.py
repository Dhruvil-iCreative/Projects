from odoo import models, fields, api


class Employee(models.Model):
    _inherit = ['sale.order']
