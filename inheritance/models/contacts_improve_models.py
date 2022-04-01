import datetime

from dateutil.relativedelta import relativedelta
from odoo import models, fields, api
from datetime import date


class ContactImprove(models.Model):
    _inherit = ["res.partner"]

    birth_date = fields.Date(default=date.today())
    age = fields.Integer(compute="_compute_age")

    def name_get(self):
        result = []
        if self._context.get("rental"):
            for rec in self:
                if rec.phone:
                    result.append((rec.id, f"{rec.name} - {rec.phone}"))
                else:
                    result.append((rec.id, f"{rec.name}"))
            return result
        return super(ContactImprove, self).name_get()

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = ['|', ('email', operator, name), ('city', operator, name)]
        return super(ContactImprove, self)._name_search(name, args=args+domain, operator=operator, limit=limit, name_get_uid=name_get_uid)

    @api.depends("birth_date")
    def _compute_age(self):
        if self.birth_date:
            dt3 = relativedelta(date.today(), self.birth_date)
            self.age = dt3.years
        else:
            self.age = 0
