# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class PriceWizard(models.TransientModel):
    _name = 'price.wizard'

    price_measurement_ids = fields.Many2many('market.research.price.measurement', string="Price Measurements", 
        default=lambda self: self._get_price_measurement_ids())

    @api.model
    def _get_price_measurement_ids(self):
        return self.env.context.get('default_price_measurement_ids') or False

    @api.multi
    def do_update_prices(self):
        self.ensure_one()