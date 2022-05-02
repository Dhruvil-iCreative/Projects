from odoo import models, fields, api


class Department(models.Model):
    _name = 'department.department'

    depart_code = fields.Integer()
    name = fields.Char(required=True)
    courses_ids = fields.Many2many(comodel_name="courses.courses", string="Course", required=True)
    classes = fields.Integer(string="NO.of Classes")
    floors = fields.Integer(string="No. of Floors")
    description = fields.Text()
