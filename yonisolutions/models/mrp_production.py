# Copyright 2022 Sodexis
# License OEEL-1 (See LICENSE file for full copyright and licensing details).

from odoo import models,_
from odoo.exceptions import UserError


class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    def action_generate_serial(self):
        if not self.lot_producing_id:
            error_msg = _('You need to supply Lot/Serial Number for products:') + self.product_id.display_name
            raise UserError(error_msg)