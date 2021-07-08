from odoo import fields, models, api, _

class ResCompany(models.Model):
    _inherit = "res.company"

    area_id = fields.Many2one('res.area', string='Area', required=True)
    atmp_dealer_code = fields.Char(string='Kode Dealer ATPM', required=True)
    branch_code = fields.Char(string='Kode Cabang', required=True)
    short_name = fields.Char(string='Singkatan')
    branch_head = fields.Char(string='Singkatan')
    is_head_office = fields.Boolean(string='Head Office', default=False)