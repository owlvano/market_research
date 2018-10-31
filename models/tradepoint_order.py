# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class TradepointOrder(models.Model):
    _name = 'market.research.tradepoint.order'
    _inherit = ['mail.thread']
    _description = _("Tradepoint Order")

    measurement_order_id = fields.Many2one('market.research.measurement.order', string="Measurement Order", default=lambda self: self._get_default_measurement_order(), required=True, track_visibility='always')
    client_id = fields.Many2one('res.partner', string="Client", required=True, track_visibility='always')
    assigned_user_id = fields.Many2one('res.users', string="Assigned User", required=True, default=lambda self: self._get_default_user_id(), track_visibility='always')

    name = fields.Char(string="Address", compute='_compute_name', store=True)
    deadline_date = fields.Date(string="Deadline", related='measurement_order_id.deadline_date')

    price_measurement_ids = fields.One2many('market.research.price.measurement', 'tradepoint_order_id', string="Price Measurements")
    progress = fields.Float(string="Progress", compute='_compute_progress')

    @api.constrains('measurement_order_id', 'client_id')
    def _check_description(self):
        self.ensure_one()
        record_count = self.env['market.research.tradepoint.order'].search_count([('measurement_order_id', '=', self.measurement_order_id.id), ('client_id', '=', self.client_id.id)])
        if record_count > 1:
            raise ValidationError(_('Tradepoint Order on client "%s" should be unique for this measurement order') % (self.client_id.display_name))

    @api.depends('client_id')
    def _compute_name(self):
        for record in self:
            record.name = _("#%d on %s") % (record.id, record.client_id.display_name)

    @api.depends('price_measurement_ids.measured_price')
    def _compute_progress(self):
        for record in self:
            if not record.price_measurement_ids:
                record.progress = 0.0
            else:
                record.progress = 100 * self.env['market.research.price.measurement'].search_count([('id', 'in', record.price_measurement_ids.ids), ('measured_price', '!=', 0.00)]) / len(record.price_measurement_ids)

    @api.model
    def _get_default_measurement_order(self):
        return self.env.context.get('default_measurement_order_id') or False

    @api.model
    def _get_default_user_id(self):
        return self.env.context.get('default_assigned_user_id') or False
