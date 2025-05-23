# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api
from odoo.exceptions import UserError

class ProjectTask(models.Model):
    _inherit = "project.task"

    # Para componer el default_code del producto automáticamente:
    shoes_default_code_prefix = fields.Char('Internal ref. prefix')
