# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api

class ProductTemplate(models.Model):
    _inherit = "product.template"

    shoes_task_id = fields.Many2one('project.task', string='Shoes model', ondelete='restrict')
    shoes_last_id = fields.Many2one('shoes.last', string='Last', ondelete='restrict')

    def _get_pair_and_variants_sync(self):
        super()._get_pair_and_variants_sync()
        if self.intrastat_duty_id:
            country = self.intrastat_duty_id.country_id,
            intrastat = self.intrastat_duty_id.intrastat_id,

            self.product_tmpl_single_id.write({
                'intrastat_duty_id': self.intrastat_duty_id.id,
                'hs_code': self.hs_code,
                'country_of_origin': country,
                'image_1920': self.image_1920,
            })

            if self.shoes_pair_weight_id.id:
                for assortment in self.product_variant_ids:
                    assortment.write({
                        'intrastat_code_id': intrastat,
                        'intrastat_origin_country_id': country,
                    })

                for pair in self.product_tmpl_single_id.product_variant_ids:
                    pair.write({
                        'intrastat_code_id': intrastat,
                        'intrastat_origin_country_id': country,
                    })


    def create_shoe_pairs(self):
        # 1) Ejecutamos el comportamiento original: creación de pares
        res = super(ProductTemplate, self).create_shoe_pairs()
        # 2) Tras crear las plantillas “single”, propagamos shoes_last_id
        for record in self:
            if record.shoes_last_id and record.product_tmpl_single_id:
                record.product_tmpl_single_id.write({
                    'shoes_last_id': record.shoes_last_id.id,
                })
        # 3) Devolvemos lo que devolvía el super (si lo hubiera)
        return res