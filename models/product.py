# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Product(models.Model):
    _name = 'market.research.product'
    _description = _("This model stores products that are being analyzed in a specific measurement order")

    product_id = fields.Many2one('product.product', string="Product", required=True)
    price = fields.Float(string="Price")

    measurement_order_id = fields.Many2one('market.research.measurement.order', string="Measurement Order")

    _sql_constraints = [
        ('product_unique',
         'UNIQUE (measurement_order_id, product_id)',
         'Products must be unique for the measurement order!')]

    @api.model
    def create(self, vals):
        record = super(Product, self).create(vals)
        
        if self.env.context.get('default_measurement_order_id'):
            record.measurement_order_id = self.env.context.get('default_measurement_order_id')

        return record