# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

class TradepointOrder(models.Model):
    _name = 'market.research.tradepoint.order'
    _description = _("This model stores certain trade points to be analyzed in a specific measurement order")

    client_id = fields.Many2one('res.partner', string="Client")
    address = fields.Char(string="Address")
    assigned_user_id = fields.Many2one('res.users', string="Assigned User")
    deadline_date = fields.Date(string="Deadline", related='measurement_order_id.deadline_date')

    measurement_order_id = fields.Many2one('market.research.measurement.order', string="Measurement Order")

    @api.model
    def create(self, vals):
        record = super(TradepointOrder, self).create(vals)
        
        if self.env.context.get('default_measurement_order_id'):
            record.measurement_order_id = self.env.context.get('default_measurement_order_id')

        return record