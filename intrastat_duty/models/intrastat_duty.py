# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class IntrastatDuty(models.Model):
    _name = 'intrastat.duty'
    _description = 'Intrastat duty'

    name = fields.Char('Name')
    intrastat_id = fields.Many2one('account.intrastat.code', string='Intrastat code')
    country_id = fields.Many2one('res.country', string='Country')
    duty = fields.Float('Duty (%)')
