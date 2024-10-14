# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    def create_assortment_serial_numbers(self):
        for record in self:
            for li in record.move_ids_without_package:
                sufix = li.product_id.campaign_id.name
                manufacturer_code = li.product_id.manufacturer_id.ref
                sequence = li.product_id.campaign_id.tracking_sequence
                serial = sufix + manufacturer_code + sequence
                # Buscar el serial, si existe sumamos uno:

        return True
