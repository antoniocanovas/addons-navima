# Copyright Serincloud SL - 2024
# License AGPL-3 - See http://www.gnu.org/licenses/agpl-3.0.html

{
    "name": "Shoes dealer",
    "summary": "Assortments, Pairs and BOM automation.",
    "version": "17.0.1.0.0",
    "category": "stock",
    "author": "Serincloud SL",
    "website": "https://www.ingenieriacloud.com",
    "license": "AGPL-3",
    "depends": [
        # ODOO:
        "crm",
        "sale_management",
        "purchase",
        "stock",
        "mrp",
        "sale_mrp",
        "project",
        "base_automation",
        "website_sale",
        "partner_commission",
        "uom",
        # PUNT:
        "partner_commission_manager_ee",
        "partner_product_attribute_value",
        # OCA:
        "product_brand",
        "product_net_weight",
        "sale_order_line_date",
        "sale_order_line_menu",
        "sale_product_template_tags",
        "product_variant_sale_price",
        "sale_product_image",
    ],
    "data": [
        "wizard/pnt_product_report_wizard_view.xml",
        "data/server_actions.xml",
        "security/ir.model.access.csv",
        "views/set_template_views.xml",
        "views/product_template_views.xml",
        "views/product_product_views.xml",
        "views/res_company_views.xml",
        "views/product_attribute_views.xml",
        "views/product_attribute_value_views.xml",
        "views/project_project_views.xml",
        "views/sale_order_views.xml",
        "views/sale_order_line_views.xml",
        "views/purchase_order_views.xml",
        "views/account_move_views.xml",
        "views/product_material_views.xml",
        "views/mrp_bom_views.xml",
        "views/sale_report_views.xml",
        "views/shoes_report_views.xml",
        "views/stock_lot_views.xml",
        "data/automatic_actions.xml",
        "reports/pnt_product_report.xml",
        "reports/pnt_product_report_template.xml",
        "views/res_users_views.xml",
        "views/stock_picking_views.xml",
        # Quito esta vista hasta que arreglemos product.product; migración v17:
#        "views/stock_orderpoint_views.xml",
        "views/account_move_line_views.xml",
        "views/shoes_pair_weight_views.xml",
        "views/assortment_pair_views.xml",
        "views/shoes_shape_views.xml",
    ],
    "installable": True,
}
