# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).


from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class ProductMaterial(models.Model):
    _inherit = "product.material"

    code = fields.Char("Code")
    display_name = fields.Char(
        string="Display name", compute="_compute_display_name", store=True
    )
    manufacturer_id = fields.Many2one(
        "res.partner", string="Manufacturer", ondelete="restrict"
    )
    manufacturer_code = fields.Char(related="manufacturer_id.ref")
    material_manufacturer_code = fields.Char(
        "MM code",
        help="Material & manufacturer concatenated code",
        store=True,
        compute="_get_material_manufacturer_code",
    )
    shoes_campaign_ids = fields.Many2many(
        "project.project", string="Campaigns", domain="[('is_shoes_campaign','=',True)]"
    )

    _sql_constraints = [
        (
            "material_manufacturer_code_unique",
            "UNIQUE(material_manufacturer_code)",
            "The Material Manufacturer Code must be unique!",
        )
    ]

    @api.constrains("material_manufacturer_code")
    def _check_material_manufacturer_code_unique(self):
        for record in self:
            if record.material_manufacturer_code:
                domain = [
                    (
                        "material_manufacturer_code",
                        "=",
                        record.material_manufacturer_code,
                    ),
                    ("id", "!=", record.id),
                ]
                if self.search_count(domain) > 0:
                    raise ValidationError(
                        _(
                            'The Material Manufacturer Code "%s" already exists!'
                            ' It must be unique.'
                        )
                        % record.material_manufacturer_code
                    )

    @api.depends("name", "code", "manufacturer_code")
    def _compute_display_name(self):
        for record in self:
            if record.name and record.code and record.manufacturer_code:
                record.display_name = (
                    f"({record.manufacturer_code}{record.code}) {record.name}"
                )
            elif record.name and record.code:
                record.display_name = f"({record.code}) {record.name}"
            elif record.name:
                record.display_name = record.name
            elif record.code:
                record.display_name = record.code
            else:
                record.display_name = False

    @api.depends("code", "manufacturer_code")
    def _get_material_manufacturer_code(self):
        for record in self:
            code = ""
            if record.code:
                code += record.code
            if record.manufacturer_code:
                code += record.manufacturer_code
            record["material_manufacturer_code"] = code
