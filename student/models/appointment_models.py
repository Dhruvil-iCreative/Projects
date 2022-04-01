from odoo import models, fields, api


class Appointments(models.Model):
    _name = 'appointment.appointment'
    _rec_name = "prof_name"

    date = fields.Datetime(string="Date&Time")
    prof_name = fields.Many2one('professor.professor', string="With", required=True)
    student_id = fields.Many2one('student.student', string="Students", required=True)
    emergency = fields.Selection([('YES', "Yes"), ('NO', "NO")])
    emergency_1 = fields.Char(string="Is it emergency??", compute="yes_no")

    @api.onchange('emergency')
    def yes_no(self):
        for rec in self:
            if rec.emergency:
                rec.emergency_1 = rec.emergency
