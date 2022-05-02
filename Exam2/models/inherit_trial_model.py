from odoo import models, fields, api


class inhertance(models.Model):
    _name = 'inheritance_trial'
    _description = 'inherit_trial'

    name = fields.Char()
    age = fields.Integer()
    city = fields.Selection([("a","Ahmedabad"),('b',"Baroda"),('s',"Surat")])

class added(models.Model):
    _inherit = "inheritance_trial"

    mobile = fields.Char()
    email = fields.Char()
