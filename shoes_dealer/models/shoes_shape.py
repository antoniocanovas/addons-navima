# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class ShoesShape(models.Model):
    _name = 'shoes.shape'
    _description = 'Shoes MRP shape'

    name = fields.Char('Name')
