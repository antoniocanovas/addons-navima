# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import fields, models, api

class AssortmentPair(models.Model):
    _name = 'assortment.pair'
    _description = 'Assortment pair'

    name = fields.Char('Name', store=True)
    product_id = fields.Many2one('product.product', string='Product variant')
    product_tmpl_id = fields.Many2one('product.template', string='Product template', related='product_id.product_tmpl_id')
    bom_qty = fields.Integer('Bom units')
    qty = fields.Integer('Pairs', compute='_get_sml_qty')
    partner_id = fields.Many2one('res.partner', string='Partner')
    sml_id = fields.Many2one('stock.move.line', string='Stock move line')
    sm_id = fields.Many2one('stock.move', string='Stock move', related='sml_id.move_id')

    @api.depends('sml_id.qty_done', 'product_id')
    def _get_sml_qty(self):
        for record in self:
            factor = 1
            if (record.x_sml_id.location_usage in ('internal', 'transit')) and (
                    record.sml_id.location_dest_usage not in ('internal', 'transit')):
                factor = -1
            record['qty'] = record.bom_qty * record.sml_id.qty_done * factor
