# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models, api

class ProductAttribute(models.Model):
    _inherit = 'product.attribute'

    partner_filter = fields.Boolean('Partner filter')