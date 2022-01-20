from odoo import fields, models, api, _


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'


    default_x_voucher_journal = fields.Many2one('account.journal', string="voucher Journal", default_model='account.user.statement')