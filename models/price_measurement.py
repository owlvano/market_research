# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Product(models.Model):
    _name = 'market.research.price.measurement'
    _description = _("This model stores product price measurement on specific tradepoints")

    product_id = fields.Many2one('product.product', string="Product", required=True)
    measured_price = fields.Float(string="Measured Price")

    tradepoint_order_id = fields.Many2one('market.research.tradepoint.order', string="Tradepoint Order")

    _sql_constraints = [
        ('product_unique',
         'UNIQUE (tradepoint_order_id, product_id)',
         'Product measurement must be unique for the tradepoint!')]

    @api.model
    def create(self, vals):
        record = super(Product, self).create(vals)
        
        if self.env.context.get('default_tradepoint_order_id'):
            record.tradepoint_order_id = self.env.context.get('default_tradepoint_order_id')

        return record