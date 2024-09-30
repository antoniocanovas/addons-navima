# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api

class StockLot(models.Model):
    _inherit = "stock.lot"

    # Depende del campo quant_id EN SML:
    def _get_assortment_pair(self):
        for record in self:
            assortment_pair = ""
            if (record.product_id.is_assortment):
                assortment_pair = "prueba"
        record['assortment_pair'] = assortment_pair

    assortment_pair = fields.Char('Assortment pair', compute='_get_assortment_pair')


    def get_assortment_pair(self):
        for lot in self:
            ap = self.env["assortment.pair"].search([("product_id", "=", record.product_id.id),('lot_id','=', record.id)])
            total = 0
            for li in ap:
                total += li.qty
            lot.pairs_count = total
    pairs_count = fields.Integer('Pairs', compute='get_assortment_pair')
