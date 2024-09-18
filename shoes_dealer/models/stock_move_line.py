# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    assortment_pair_ids = fields.One2many('assortment.pair','sml_id', string='Assortment pairs')