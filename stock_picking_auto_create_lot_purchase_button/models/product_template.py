# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = "product.template"

    auto_create_lot = fields.Boolean(default=True)