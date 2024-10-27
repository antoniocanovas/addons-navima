# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api
from odoo.exceptions import UserError

class ProjectProject(models.Model):
    _inherit = "project.project"


    shoes_color_chart_ids = fields.Many2many('shoes_color_chart','project_id')
