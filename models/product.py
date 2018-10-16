# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class Product(models.Model):
    _name = 'market.research.product'
    _description = _("Researched Product")

    product_id = fields.Many2one('product.product', string="Product", required=True)
    price = fields.Float(string="Price")

    measurement_order_id = fields.Many2one('market.research.measurement.order', string="Measurement Order", default=lambda self: self._get_default_measurement_order())

    _sql_constraints = [
        ('product_unique',
         'UNIQUE (measurement_order_id, product_id)',
         _('Products must be unique for the measurement order!'))]

    @api.model
    def _get_default_measurement_order(self):
        return self.env.context.get('default_measurement_order_id') or False

    @api.multi
    @api.onchange('product_id')
    def get_last_product_price(self):
        self.ensure_one()
        if self.product_id:
            self.price = self.search([('product_id','=',self.product_id.id)], order='create_date desc', limit=1).price or False
        return False
