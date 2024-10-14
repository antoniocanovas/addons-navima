# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class ProductAttributeValueGroup(models.Model):
    _name = 'product.attribute.value.group'
    _description = 'Product attribute value Group'

    name = fields.Char('Name')
    attribute_id = fields.Many2one('product.attribute', string='Attribute')
