# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api
from odoo.exceptions import UserError

class ProjectProject(models.Model):
    _inherit = "project.project"

    is_shoes_campaign = fields.Boolean('Is shoes campaign', default=True)

    # Datos comunes para creación de productos desde tareas:
    brand_id = fields.Many2one('product.brand', string="Brand")
