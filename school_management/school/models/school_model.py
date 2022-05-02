# -*- coding: utf-8 -*-

from odoo import models, fields, api


class School(models.Model):
    _name = 'school.school'
    _description = 'school.school'

    name = fields.Char(required=True)
    departments_ids = fields.Many2many("department.department", string="Departments")
    course_ids = fields.Many2many("courses.courses", string="Course")

    # student_id=fields.One2many("student.student","school_id_1",string="Students")
    @api.onchange('departments_ids')
    def Special_Command(self):
        ids = []
        for rec in self:
            ids = rec.departments_ids.courses_ids.ids
            rec.write({"course_ids": [(6, 0, ids)]})
