# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class TradepointOrder(models.Model):
    _name = 'market.research.tradepoint.order'
    _description = _("This model stores certain trade points to be analyzed in a specific measurement order")

    client_id = fields.Many2one('res.partner', string="Client", required=True)
    assigned_user_id = fields.Many2one('res.users', string="Assigned User", required=True)

    address = fields.Char(string="Address")
    deadline_date = fields.Date(string="Deadline", related='measurement_order_id.deadline_date')

    measurement_order_id = fields.Many2one('market.research.measurement.order', string="Measurement Order", default=lambda self: self._get_default_measurement_order())
    price_measurement_ids = fields.One2many('market.research.price.measurement', 'tradepoint_order_id', string="Price Measurements")

    _sql_constraints = [
        ('tradepoint_order_unique',
         'UNIQUE (measurement_order_id, client_id)',
         'Clients must be unique for the measurement order!')]

    @api.model
    def _get_default_measurement_order(self):
        return self.env.context.get('default_measurement_order_id') or False