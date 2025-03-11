# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models, api

class ProductMaterial(models.Model):
    _name = 'product.material'
    _description = 'Product material'

    name = fields.Char('Name' , translate=True)
    image = fields.Binary('Image', copy=False)
    comment = fields.Html('Comments',  copy=False , translate=True)
    is_skin = fields.Boolean('Skin',  copy=False)
    display_name = fields.Char(string='Display name', compute='_compute_display_name')

    @api.depends('name', 'code')
    def _compute_display_name(self):
        for record in self:
            if record.name and record.code:
                record.display_name = f"{record.name} ({record.code})"
            elif record.name:
                record.display_name = record.name
            elif record.code:
                record.display_name = record.code
            else:
                record.display_name = False