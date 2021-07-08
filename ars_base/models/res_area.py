# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class ResArea(models.Model):
    _name = 'res.area'
    _description = 'Area'

    name = fields.Char(string='Nama Area', required=True)
    code = fields.Char(string='Kode Area', required=True)
    short_name = fields.Char(string='Singkatan')
    active = fields.Boolean(default=True, help="Set active to false to hide the Account Tag without removing it.")
