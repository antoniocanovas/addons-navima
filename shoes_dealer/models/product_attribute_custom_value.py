# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api

class ProductAttributeCustomValue(models.Model):
    _inherit = 'product.attribute.custom.value'

    assortment_pair = fields.Char('Assortment pairs', readonly=True, store=True)
    pairs_count = fields.Integer('Pairs count', readonly=True)
    
    @api.depends('custom_value')
    def _get_assortment_pair(self):
        for record in self:
            size_attribute = self.env.company.size_attribute_id
            sale_line_product = record.sale_order_line_id.product_id
            sale_line_product_color = sale_line_product.color_attribute_id
            shoes_pair_model = sale_line_product.product_tmpl_single_id

            if sale_line_product.is_assortment:
                # Quitar espacios del campo custom del surtido:
                customvalue = record.custom_value.replace(" ", "")
                customvalues = customvalue.split(",")

                # Chequear que las tallas o cantidades introducidas son válidas y el par está creado:
                cleanvalues, sizes, pairs, pairs_count = [], [], [], 0
                for li in customvalues:
                    element = li.split("x")
                    # Para tallas (encontrar si existe la talla y color en el par):
                    color_attribute_value_id = sale_line_product_color
                    size_attribute_value_id = env['product.attribute.value'].search(
                        [('attribute_id', '=', size_attribute.id), ('name', '=', element[0])])
                    if not size_attribute_value_id.id:
                        raise UserError("La talla " + str(element[0]) + " no existe en el sistema.")

                    pppair = env['product.product'].search([('color_attribute_id', '=', color_attribute_value_id.id),
                                                            ('size_attribute_id', '=', size_attribute_value_id.id),
                                                            ('product_tmpl_id', '=', shoes_pair_model.id)])
                    if not pppair.id:
                        raise UserError("No encuentro el par suelto de talla " + str(
                            element[0]) + " y color " + color_attribute_value_id.name + " en este modelo.")

                    # Para cantidades (ok):
                    try:
                        qty = int(element[1])
                    except:
                        raise UserError(element[1] + ", no parece una cantidad válida. Indica un número entero válido.")
                    sizes.append(element[0])
                    pairs.append(element[1])
                    pairs_count += int(element[1])

                # OK, guardamos valores:
                cleanvalues.append(sizes)
                cleanvalues.append(pairs)
                record.write({'assortment_pair': cleanvalues, 'pairs_count': pairs_count})