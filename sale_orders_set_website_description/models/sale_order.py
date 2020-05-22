# -*- coding: utf-8 -*-
import logging
_logger = logging.getLogger(__name__)

from odoo import api, models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'
                                
    @api.model    
    def cron_sale_orders_set_website_description(self):
        self.env.cr.execute("UPDATE sale_order_line SET website_description = NULL WHERE id > 0")
        self.env.cr.execute("UPDATE sale_order SET website_description = (SELECT website_description FROM sale_order_template WHERE id = order_template_id)")