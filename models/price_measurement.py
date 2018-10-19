# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class PriceMeasurement(models.Model):
    _name = 'market.research.price.measurement'
    _description = _("Product Price Measurement")

    product_id = fields.Many2one('product.product', string="Product", required=True)
    product_name = fields.Char(string="Product Name", related='product_id.name')
    product_default_code = fields.Char(string="Internal Reference", related='product_id.default_code')

    measured_price = fields.Float(string="Measured Price")

    tradepoint_order_id = fields.Many2one('market.research.tradepoint.order', string="Tradepoint Order", default=lambda self: self._get_default_tradepoint_order())
    assigned_user_id = fields.Many2one('res.users', string="Assigned User", related='tradepoint_order_id.assigned_user_id', store=True)
    client_id = fields.Many2one('res.partner', string="Client", related='tradepoint_order_id.client_id', store=True)

    _sql_constraints = [
        ('product_unique',
         'UNIQUE (tradepoint_order_id, product_id)',
         _('Product measurement must be unique for the tradepoint!'))]

    @api.model
    def _get_default_tradepoint_order(self):
        return self.env.context.get('default_tradepoint_order_id') or False

    @api.model
    def create(self, values):
        record = super(PriceMeasurement, self).create(values)

        record.product_id = values['product_id']
        record.tradepoint_order_id = values['tradepoint_order_id']  
        
        return record