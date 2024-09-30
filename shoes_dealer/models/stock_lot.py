# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api

class StockLot(models.Model):
    _inherit = "stock.lot"

    # Cuando se crea un STOCK.QUANT EN SML:
#    def _get_assortment_pair(self):
#        for record in self:
#            assortment_pair = ""
#        record['assortment_pair'] = assortment_pair

    assortment_pair = fields.Char('Assortment pair', store=True,
#                                  compute='_get_assortment_pair'
                                  )

    # Llevar la combinación del pedido de venta o compra y número de pares, al lote:
 #   def _get_shoes_pair_count(self):
 #       for record in self:
 #           count = 0
 #           for li in record.invoice_line_ids:
 #               count += li.pairs_count
 #           record['pairs_count'] = count
    pairs_count = fields.Integer('Pairs', store=False,
 #                                compute='_get_shoes_pair_count'
                                 )
