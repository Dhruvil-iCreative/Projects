# -*- coding: utf-8 -*-

from odoo import models, fields, api


class every(models.Model):
    _name = 'every.every'
    _inherit='hospital.hospital'
    _description = 'every.every'
    image = fields.Binary()
    t_doc = fields.Char(string="Treatment Doctor")
    t_doc_number = fields.Char(string="Contact Number")
    t_doc_exp = fields.Integer(string="Experience")
    t_doc_qua = fields.Char(compute="_value_pc_1",store=True,string="Level of Doctor")
    state = fields.Selection([("start","Start"),("in_process","InProcess"),("confirm","Confirm"),("cancel","Cancel")],default="start",string="Status")
    partner_id = fields.Many2one("res.partner")
    city_1 = fields.Char(related="partner_id.city",readonly=False)

    def action_process(self):
        self.state = "in_process"

    def action_confirm(self):
        self.state = "confirm"

    def action_cancel(self):
        self.state = "cancel"

    @api.depends('t_doc_exp')
    def _value_pc_1(self):
        for record in self:
            if record.t_doc_exp<=1:
                record.t_doc_qua="Beginner"
            elif 1<record.t_doc_exp<5:
                record.t_doc_qua="Medium"
            else:
                record.t_doc_qua="Advance"

    @api.depends('visit_fee', 'medication_fee')
    def _value_pc(self):
        for record in self:
            record.total_fee = float(record.visit_fee) + float(record.medication_fee)

    def wiz_open(self):
        return self.env['ir.actions.act_window']._for_xml_id("every.discount_apply_action")

    def wiz_open2(self):
        return self.env['ir.actions.act_window']._for_xml_id("every.penalty_add_action")
        # return {"type":"ir.actions.act_window",
        #         "res_model":"discount.apply.wiz",
        #         "view_mode":"form",
        #         "target":"new"}

    def hospital_open(self):
        return self.env['ir.actions.act_window']._for_xml_id("hospital.hospital_action_window")


