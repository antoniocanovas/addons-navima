# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api


class StockMove(models.Model):
    _inherit = "stock.move"

    # Comercialmente en cada Albaran quieren saber cuántos pares se han vendido:
# V16 (para borrar si funciona v17, porque ya no existe quantity_done):    @api.depends("product_id", "quantity_done")
#    def _get_shoes_stock_move_pair_count(self):
#        for record in self:
#            record["pairs_count"] = record.product_id.pairs_count * record.quantity_done

    @api.depends('move_line_ids.quantity')
    def _get_shoes_stock_move_pair_count(self):
        for move in self:
            move.pairs_count = sum(line.quantity for line in move.move_line_ids) * self.product_id.pairs_count
    pairs_count = fields.Integer(
        "Pairs", store=True, compute="_get_shoes_stock_move_pair_count"
    )
