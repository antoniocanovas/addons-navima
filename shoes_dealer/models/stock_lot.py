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
            total = 0
            if (lot.product_id.is_assortment) and (lot.product_id.product_tmpl_single_id.id):
                pair_model = lot.product_id.product_tmpl_single_id
                aps = self.env['assortment.pair'].search([('product_tmpl_id', '=', pair_model.id), ('lot_id', '=', lot.id)])
                for li in aps:
                    total += li.qty
            lot.pairs_count = total

    pairs_count = fields.Integer('Assortment pairs count', compute='get_assortment_pair')
