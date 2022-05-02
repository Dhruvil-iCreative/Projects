from odoo import models, fields, api


class RentalType(models.Model):
    _name = 'rental.type'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    code = fields.Integer(tracking=True)
    description = fields.Text(tracking=True)

    # @api.model
    # def create(self, vals):
    #     print("*****************Values***********", vals)
    #     print("____________________self_______________", self)
    #     rtn = super(RentalType, self).create(vals)
    #     print("++++++++++++++++return+++++++++++++++", rtn)
    #     return rtn

    def wizard_perform(self):
        return self.env['ir.actions.act_window']._for_xml_id("rental_management.rental_type_wiz_views_action_window")

    # def write(self, values):
    #     values.update({
    #         'description': 'This field has been edited'
    #     })
    #     res = super(RentalType, self).write(values)
    #     return res

    def write_name(self):
        self.write({
            'description': 'This field has been edited'
        })

    def unlink(self):
        res = super(RentalType, self).unlink()
        return res

    # 6
    # moves = self.env['rental.type'].browse(self.env.context.get('active_ids'))