# Copyright Serincloud SL - Ingenieriacloud.com


from odoo import fields, models, api, _
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = "product.template"

    manufacturer_id = fields.Many2one(
        "res.partner", string="Manufacturer", store=True, copy=True
    )
