from odoo import models, fields, api


class hospital(models.Model):
    _name = 'hospital.hospital'
    _inherit = ["mail.thread","mail.activity.mixin"]
    _description = 'hospital.hospital'

    fname = fields.Char()
    lname=fields.Char()
    image=fields.Binary()
    mobile=fields.Char()
    email=fields.Char()
    gender=fields.Selection([('m',"Male"),("f","Female"),("o","Other")])
    city=fields.Selection([("a","Ahmedabad"),("b","Baroda"),("r","Rajkot"),("s","Surat")])

    disease=fields.Selection([("d","Dangue"),("v","Viral"),("m","Maleria"),("d","Diarhea")])
    visit_fee = fields.Integer()
    medication_fee=fields.Integer()
    total_fee = fields.Float(compute="_value_pc", store=True)
    treatement_mode=fields.Selection([('o',"Operation"),("s","Surgery"),("m","Medicines")])
    treatement_cost=fields.Float()
    treatement_date=fields.Date()
    treatement_disc=fields.Char()
    rec_opt=fields.Selection([("y","Yes"),("n","No")],string="Recommendation Option")
    rec_hos=fields.Char(string="Recommended Hospital")
    rec_doc=fields.Char(string="Doctor name")
    patient_count=fields.Integer(compute="count_patients",store=True)

    @api.depends('visit_fee','medication_fee')
    def _value_pc(self):
        for record in self:
            record.total_fee = float(record.visit_fee) + float(record.medication_fee)

    def back_to_every(self):
        return self.env['ir.actions.act_window']._for_xml_id("every.action_window")

    @api.depends('mobile')
    def count_patients(self):
        for record in self:
            patient_count=self.search_count([('mobile','=',record.id)])
            record.patient_count = patient_count


