# Copyright
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo import fields, models, api
from odoo.exceptions import UserError

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    def _get_duty_estimation(self):
        for record in self:
            total = 0
            record['duty_estimation'] = total
    duty_estimation = fields.Monetary('Duty estimation', compute='_get_duty_estimation')