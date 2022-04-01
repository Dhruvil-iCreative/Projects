from odoo import models, fields, api


class SaleOrderDefaultWiz(models.TransientModel):
    _name = "default.wiz"

    customer = fields.Char()
    cus_email = fields.Char()
    sale_person = fields.Char()
    sale_person_contact = fields.Char()
    payment_terms = fields.Char()

    @api.model
    def default_get(self, fields):
        vals = super(SaleOrderDefaultWiz, self).default_get(fields)
        customer = self.env['sale.order'].browse([self.env.context.get('active_id')])
        vals.update({
            'customer': customer.partner_id.name,
            'cus_email': customer.email,
            'sale_person': customer.user_id.name,
            'sale_person_contact': customer.user_id.phone,
            'payment_terms': customer.payment_term_id.name,
        })
        return vals
