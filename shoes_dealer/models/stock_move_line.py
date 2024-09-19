# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api


class StockMoveLine(models.Model):
    _inherit = "stock.move.line"

    assortment_pair_ids = fields.One2many('assortment.pair','sml_id', string='Assortment pairs')


    def _create_assortment_pair(self):
        for record in self:
            # Sólo para surtidos:
            if not record.product_id.is_assortment:
                continue
            # Diferencia entre compra y ventas:
            if record.move_id.sale_line_id.id: origin = record.move_id.sale_line_id
            if record.move_id.purchase_line_id.id: origin = record.move_id.purchase_line_id.sale_line_id

            # Si el valor del surtido es personalizado, crear assortment.pair desde valor custom:
            if record.product_id.assortment_attribute_id.is_custom and origin.product_custom_attribute_value_ids.ids:
                customvalue = origin.product_custom_attribute_value_ids[0].assortment_pair
                elements = [list(map(int, item.split(","))) for item in customvalue.split(";")]
                sizes, quantity, products, i = elements[0], elements[1], elements[2], 0

                for p in products:
                    self.env['assortment.pair'].create({'product_id': p, 'bom_qty': quantity[i], 'sml_id': record.id})

            # Surtido normal:
            if record.product_id.assortment_attribute_id.is_custom == False:
                # raise UserError('surtido estándar')
                return True
