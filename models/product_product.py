# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models

class ProductProduct(models.Model):
    _inherit = "product.product"

    @api.multi
    def name_get(self):
        if self.env.context.get('product_default_name_get'):
            # default names
            result = []
            for product in self.sudo():
                result.append((product.id, product.name))
            return result
        else:
            #call original name_get
            return super(ProductProduct, self).name_get()
