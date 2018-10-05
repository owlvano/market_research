# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class PriceMeasurement(models.Model):
    _name = 'market.research.price.measurement'
    _description = _("Product Price Measurement")

    product_id = fields.Many2one('product.product', string="Product", required=True)
    measured_price = fields.Float(string="Measured Price")

    tradepoint_order_id = fields.Many2one('market.research.tradepoint.order', string="Tradepoint Order", default=lambda self: self._get_default_tradepoint_order())

    _sql_constraints = [
        ('product_unique',
         'UNIQUE (tradepoint_order_id, product_id)',
         'Product measurement must be unique for the tradepoint!')]

    @api.model
    def _get_default_tradepoint_order(self):
        return self.env.context.get('default_tradepoint_order_id') or False

    @api.model
    def create(self, values):
        record = super(PriceMeasurement, self).create(values)

        record.product_id = values['product_id']
        record.tradepoint_order_id = values['tradepoint_order_id']  
        
        return record