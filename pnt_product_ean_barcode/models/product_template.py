# Copyright puntsistemes.es

from gtin import GTIN

from odoo import _, api, fields, models
from odoo.exceptions import UserError


class ProductTemplate(models.Model):
    _inherit = ["product.template"]

    pnt_ean_required = fields.Boolean(
        string="EAN required", related="categ_id.pnt_ean_required"
    )
    barcode = fields.Char(copy=True, tracking=True)
    hide_internal_ean_sequence = fields.Boolean(
        string="Hide Internal EAN Sequence",
        compute="_compute_hide_internal_ean_sequence",
        store=False,
    )

    @api.depends()  # sin dependencias, se recalcula al abrir
    def _compute_hide_internal_ean_sequence(self):
        Param = self.env["ir.config_parameter"].sudo()
        hide = Param.get_param(
            "pnt_product_ean_barcode.internal_ean_sequence", default="False"
        )
        for tmpl in self:
            tmpl.hide_internal_ean_sequence = hide != "True"

    hide_public_ean_sequence = fields.Boolean(
        string="Hide Internal EAN Sequence",
        compute="_compute_hide_public_ean_sequence",
        store=False,
    )

    @api.depends()  # sin dependencias, se recalcula al abrir
    def _compute_hide_public_ean_sequence(self):
        Param = self.env["ir.config_parameter"].sudo()
        hide = Param.get_param(
            "pnt_product_ean_barcode.public_ean_sequence", default="False"
        )
        for tmpl in self:
            tmpl.hide_public_ean_sequence = hide != "True"

    def create_default_code(self):
        code = self.env.context.get("code")
        seq = self.env["ir.sequence"].search([("code", "=", code)], limit=1)
        pnt_ean14_prefix = seq.pnt_ean14_prefix

        products = self.product_variant_ids or self
        for product in products:
            if not product.barcode:
                barcode = self.env["ir.sequence"].next_by_code(code)
                if len(barcode) == 12:
                    if pnt_ean14_prefix:
                        barcode = f"{pnt_ean14_prefix}{barcode}{GTIN(raw=barcode).check_digit}"  # noqa: E501
                    else:
                        barcode = f"{barcode}{GTIN(raw=barcode).check_digit}"
                    product.write({"barcode": barcode})
                else:
                    raise UserError(
                        _("The product %s does not have a valid EAN length")
                        % product.display_name
                    )
