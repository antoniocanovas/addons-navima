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
    qty = fields.Integer('Pairs')
    partner_id = fields.Many2one('res.partner', string='Partner')
    sml_id = fields.Many2one('stock.move.line', string='Stock move line')
    sm_id = fields.Many2one('stock.move', string='Stock move', related='sml_id.move_id')
