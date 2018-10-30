# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class Product(models.Model):
    _name = 'market.research.product'
    _description = _("Researched Product")

    product_id = fields.Many2one('product.product', string="Product", required=True)
    price = fields.Float(string="Price")

    measurement_order_id = fields.Many2one('market.research.measurement.order', string="Measurement Order", default=lambda self: self._get_default_measurement_order())

    _sql_constraints = [
        ('product_unique',
         'CHECK (1=1)',
         _('Products must be unique for the measurement order!'))]  #manual SQL constraint removal (in a separate branch)

    @api.constrains('measurement_order_id', 'product_id')
    def _check_description(self):
        self.ensure_one()
        record_count = self.env['market.research.product'].search_count([('measurement_order_id', '=', self.measurement_order_id.id), ('product_id', '=', self.product_id.id)])
        if record_count > 1:
            raise ValidationError(_('Product "%s" should be unique for this measurement order') % (self.product_id.display_name))

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
