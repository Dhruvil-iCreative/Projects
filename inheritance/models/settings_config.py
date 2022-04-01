from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_checked = fields.Boolean("Test check")
    description = fields.Html(string='Description')
    company_id = fields.Many2one('res.company', string="Company", required = False)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['is_checked'] = self.env['ir.config_parameter'].get_param(
            'inheritance.is_checked')
        res['description'] = self.env['ir.config_parameter'].get_param(
            'inheritance.description')
        res['company_id'] = int(self.env['ir.config_parameter'].get_param(
            'inheritance.company_id'))
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param(
            'inheritance.is_checked', self.is_checked)
        self.env['ir.config_parameter'].set_param(
            'inheritance.description', self.description)
        self.env['ir.config_parameter'].set_param(
            'inheritance.company_id', self.company_id.id)
        super(ResConfigSettings, self).set_values()

    @api.onchange('is_checked')
    def _onchange_is_checked(self):
        for rec in self:
            if not rec.is_checked:
                rec.description = False
                rec.company_id = False
