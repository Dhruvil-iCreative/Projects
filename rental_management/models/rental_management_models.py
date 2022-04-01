from odoo import models, fields, api
from odoo.exceptions import ValidationError


class RentalManagement(models.Model):
    _name = 'rental.management'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char(required=True, tracking=True)
    customer_id = fields.Many2one(comodel_name="res.partner", string="Customer", tracking=True)
    rental_type_id = fields.Many2one(comodel_name="rental.type", string="Rental Type")
    start_date = fields.Datetime()
    end_date = fields.Datetime()
    rental_product_id = fields.Many2one(comodel_name="product.template", string="Rental Product")
    price = fields.Float(related="rental_product_id.list_price")
    state = fields.Selection([('draft', 'Draft'), ('waiting', 'Waiting'), ('approve', 'Approve'), ('cancel', 'Cancel')],
                             default="draft", string="Status", tracking=True)

    def action_draft(self):
        self.state = "draft"

    def action_waiting(self):
        self.state = "waiting"

    def action_approve(self):
        self.state = "approve"

    def action_cancel(self):
        self.state = "cancel"

    @api.depends('customer_id')
    def press_button(self):
        display_msg = "Button Pressed BY " + str(self.customer_id.name)
        return self.message_post(body=display_msg)

    @api.constrains('end_date', 'start_date')
    def date_constrains(self):
        for rec in self:
            if rec.end_date < rec.start_date:
                raise ValidationError('Sorry, End Date Must be greater Than Start Date...')
