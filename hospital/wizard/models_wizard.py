from odoo import models, fields


class hospital_wizard(models.TransientModel):
    _name = 'hospital.wizard'


    fname = fields.Char()
    lname=fields.Char()
    image=fields.Binary()
    mobile=fields.Char()
    email=fields.Char()

    def print(self):
        print('yyyyyy')
