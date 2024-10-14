# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def create_assortment_serial_numbers(self):
        for record in self:
            for li in record.move_ids_without_package:
                lots = []
                sufix = li.product_id.campaign_id.name
                manufacturer_code = li.product_id.manufacturer_id.ref
                if not sufix or not manufacturer_code:
                    continue

                for i in li.product_uom_qty:
                    sequence = str(li.product_id.campaign_id.tracking_sequence + 100000)[-5:]

                    serial = sufix + manufacturer_code + sequence
                    # Buscar el serial, si existe sumamos uno:
                    lot = self.env['stock.lot'].search([('product_id','=',li.product_id.id),('name','=',serial)])
                    if not lot.id:
                        lot = self.env['stock.lot'].create({'product_id':li.product_id.id, 'name':serial})
                    lots.append(lot.id)
                li['lot_ids'] = [(4,lots.ids)]

        return True
