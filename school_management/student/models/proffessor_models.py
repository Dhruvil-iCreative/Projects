from odoo import models, fields, api


class Professor(models.Model):
    _name = 'professor.professor'

    name = fields.Char(string="Professor Name", required=True)
    age = fields.Integer()
    specialization_course_id = fields.Many2one('courses.courses', string="Specialization", required=True)
    experience = fields.Integer()
    online = fields.Boolean('Teaches Online??')
    scheduled_appnt_id = fields.One2many('appointment.appointment', 'prof_name', string="Scheduled_appointment")
    appointments = fields.Integer(string="No of Appointments", compute='count_appointments')

    def count_appointments(self):
        for rec in self:
            appnts = self.env['appointment.appointment'].search_count([('prof_name', '=', rec.id)])
            rec.appointments = appnts
