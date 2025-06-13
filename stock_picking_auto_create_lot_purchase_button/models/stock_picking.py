# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import _, fields, models, api


class StockPicking(models.Model):
    _inherit = "stock.picking"


    # Truco para llamar a un método privado desde un botón para el método de stock-picking-auto-create-lot
    # (requiere que el TIPO DE MOVIMIENTO tenga activada la función y también el producto que será por defecto):
    def set_auto_lot(self):
        for picking in self:
            picking.sudo()._set_auto_lot()