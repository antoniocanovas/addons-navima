# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models, api

class ProductMaterial(models.Model):
    _inherit = 'product.material'

    code = fields.Char('Code')
    display_name = fields.Char(string='Display name', compute='_compute_display_name')

    @api.depends('name', 'code')
    def _compute_display_name(self):
        for record in self:
            if record.name and record.code:
                record.display_name = f"({record.code}) {record.name}"
            elif record.name:
                record.display_name = record.name
            elif record.code:
                record.display_name = record.code
            else:
                record.display_name = False