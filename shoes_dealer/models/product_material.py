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
