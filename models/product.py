# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import odoo.addons.decimal_precision as dp

class Product(models.Model):
    _name = 'market.research.product'
    _description = _("This model stores products that are being analyzed in a specific measurement order")

    product_id = fields.Many2one('product.product', string="Product")
    price = fields.Float(string="Price", digits=dp.get_precision('Product Price'))

    measurement_order_id = fields.Many2one('market.research.measurement.order', string="Measurement Order")

    @api.model
    def create(self, vals):
        record = super(Product, self).create(vals)
        
        if self.env.context.get('default_measurement_order_id'):
            record.measurement_order_id = self.env.context.get('default_measurement_order_id')

        return record