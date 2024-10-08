# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class ShoesShape(models.Model):
    _name = 'shoes.shape'
    _description = 'Shoes MRP shape'

    name = fields.Char('Name')
    heel_type = fields.Char('Heel type')
    heel_height = fields.Float('Heel height')
    platform_height = fields.Float('Platform height')
    platform_material_id = fields.Many2one('product.material', string="Platform material")
    sole_material_main_id = fields.Many2one('product.material', string="Sole material")
    sole_material_secondary_id = fields.Many2one('product.material', string="Sole material 2")
    sole_material_main_percent = fields.Float('Sole main mat. (%)')
    sole_material_secondary_percent = fields.Float('Sole second mat. (%)')
    insole_material_id = fields.Char('Insole type')
    insole_material_percent = fields.Float('Insole material (%)')
    description = fields.Text('Description', translate=True)
