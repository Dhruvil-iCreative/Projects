import datetime

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api
from datetime import date


class ContactImprove(models.Model):
    _inherit = ["res.partner"]

    birth_date = fields.Date(default=date.today())
    age = fields.Integer(compute="_compute_age")

    @api.depends("birth_date")
    def _compute_age(self):
        if self.birth_date:
            dt3 = relativedelta(date.today(), self.birth_date)
            self.age = dt3.years
        else:
            self.age = 0

