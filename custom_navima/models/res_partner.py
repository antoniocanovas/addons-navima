# Copyright 2023 Serincloud SL - Ingenieriacloud.com

from odoo import fields, models, api


class ResPartner(models.Model):
    _inherit = "res.partner"


    # Campos de migración facilitados por el cliente, se pueden eliminar en un futuro para PROVEEDORES (de momento):
    mig_subcuenta = fields.Char('mig_subcuenta')
    mig_agente = fields.Char('mig_agente')
    mig_inconterm = fields.Char('mig_inconterm')
    mig_fpago = fields.Char('mig_fpago')
    mig_aseguradora = fields.Char('mig_aseguradora')
    mig_concedido = fields.Char('mig_concedido')
    mig_posicionfiscal = fields.Char('mig_posicionfiscal')
    mig_responsableinterno = fields.Char('mig_posicionfiscal')
    mig_provincia = fields.Char('mig_provincia')
    mig_vat = fields.Char('mig_vat')