from odoo import models, fields, api


class Courses(models.Model):
    _name = 'courses.courses'

    course_code = fields.Integer()
    name = fields.Char(required=True)
    duration = fields.Integer(string="Duration in Months")
    duration_year = fields.Float(compute="duration_in_year", string="Duration in Years")
    description = fields.Text()
    fees = fields.Integer(required=True)

    @api.depends('duration')
    def duration_in_year(self):
        for record in self:
            record.duration_year = record.duration/12
