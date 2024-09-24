# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api
from odoo.exceptions import UserError

class ProjectTask(models.Model):
    _inherit = "project.task"

    is_shoes_campaign = fields.Boolean('Is shoes campaign', related='project_id.is_shoes_campaign')

    # Datos comunes para creación de productos desde tareas:

    product_brand_id = fields.Many2one('product.brand', related='project_id.product_brand_id')
    manufacturer_id = fields.Many2one('res.partner', string='Manufacturer')
    gender = fields.Selection(
        [("man", "Man"), ("woman", "Woman"), ("unisex", "Unisex")],
        string="Gender",
        copy=True,
        store=True,
    )

    shoes_pair_weight_id = fields.Many2one(
        "shoes.pair.weight", string="Pair Weight", default=False
    )
    shoes_hscode_id = fields.Many2one(
        "shoes.hs.code", string="Shoes HS Code", default=False
    )

    material_id = fields.Many2one(
        "product.material", string="Material", store=True, copy=True
    )

    product_tmpl_id = fields.Many2one('project.template', string="Product")

    def create_shoe_model(self):
        if not self.product_tmpl_id.id:
            newproduct = self.env['product.template'].create({
                'name': self.name,
                'shoes_campaign_id':self.project_id.id,
                'product_brand_id':self.product_brand_id.id,
                'manufacturer_id':self.manufacturer_id.id,
                'gender': self.gender,
                'shoes_pair_weight_id': self.shoes_pair_weight_id.id,
                'shoes_hscode_id': self.shoes_hscode_id.id,
                'material_id': self.material_id.id,
            })
            self.product_tmpl_id = newproduct.id
