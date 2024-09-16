# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models, api

class ProductTemplateAttributeLine(models.Model):
    _inherit = 'product.template.attribute.line'

    material_id = fields.Many2one('product.material', related='product_tmpl_id.material_id')
