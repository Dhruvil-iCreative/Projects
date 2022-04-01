# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Student(models.Model):
    _name = 'student.student'
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = 'student.student'
    _rec_name = "fname"

    fname = fields.Char(required=True, tracking=True)
    lname = fields.Char()
    image = fields.Binary()
    mobile = fields.Char(required=True, tracking=True)
    email = fields.Char(required=True, tracking=True)
    gender = fields.Selection([('m', "Male"), ("f", "Female"), ("o", "Other")])
    city = fields.Selection([("a", "Ahmedabad"), ("b", "Baroda"), ("r", "Rajkot"), ("s", "Surat")])
    school_id = fields.Many2one(comodel_name="school.school", string="School", required=True, tracking=True)
    departments_ids = fields.Many2many(string="Department", related="school_id.departments_ids")
    courses_ids = fields.Many2many("courses.courses", string="Courses")
    appointment_id = fields.One2many('appointment.appointment', 'student_id', string="Appointment", tracking=True)
    task_ids = fields.Many2many("tasks.tasks", string="Task Checklist", tracking=True)
    checklist_progress = fields.Float(compute="tasks_progress", string="Progress", store=True, default=0.0)
    tod = fields.Datetime(comodel_name='Date current action', default=lambda self: fields.Datetime.now(),
                          string="Apply On")
    appointment_count = fields.Integer(compute="_compute_appointment_count")

    @api.depends('task_ids')
    def tasks_progress(self):
        """return the value of the progress done after clicking the checkboxes"""
        for rec in self:
            total_len = self.env['tasks.tasks'].search_count([])
            check_list_len = len(rec.task_ids)
            if total_len != 0:
                rec.checklist_progress = (check_list_len * 100) / total_len

    @api.onchange('departments_ids')
    def Special_Command(self):
        for rec in self:
            ids = rec.departments_ids.courses_ids.ids
            rec.write({"courses_ids": [(6, 0, ids)]})

    def _compute_appointment_count(self):
        for rec in self:
            rec.appointment_count = self.env['appointment.appointment'].search_count([("student_id", "=", rec.id)])

    def appointment_domain_list(self):
        return {
            'name': 'Appointment',
            'domain': [('student_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'appointment.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window'
        }
