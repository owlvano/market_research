# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.fields import Date

class MeasurementOrder(models.Model):
    _name = 'market.research.measurement.order'
    _inherit = ['mail.thread']
    _description = _("Measurement Order")

    name = fields.Char(string="Name", translate=True, track_visibility='always')
    responsible_id = fields.Many2one('res.users', string="Responsible User", track_visibility='always')
    default_assigned_user_id = fields.Many2one('res.users', string="Default Assigned User")
    deadline_date = fields.Date(string="Deadline")
    approval_date = fields.Date(string="Approval Date")
    stage = fields.Selection([
            ('draft', 'Draft'), 
	    	('planned', 'Planned'), 
	    	('completed', 'Completed'), 
	    	('cancelled', 'Cancelled')
            ],default='draft', track_visibility='onchange')

    tradepoint_order_ids = fields.One2many('market.research.tradepoint.order', 'measurement_order_id', string="Trade Points")
    product_ids = fields.One2many('market.research.product', 'measurement_order_id', string="Products")

    @api.model
    def create(self, vals):
        record = super(MeasurementOrder, self).create(vals)
        
        record.name = _("Measurement order #%d since %s") % (record.id, Date.from_string(record.create_date).strftime("%d.%m.%Y"))

        return record
           
    @api.multi
    def action_assign(self):
        self.ensure_one()

        for tradepoint_id in self.tradepoint_order_ids:
            for product_id in self.product_ids:
                self.env['market.research.price.measurement'].create({'tradepoint_order_id': tradepoint_id.id, 'product_id': product_id.product_id.id})
            tradepoint_id.write({'stage': 'planned'})
        self.write({'stage': 'planned'})
        return True

    @api.multi
    def action_complete(self):
        self.ensure_one()

        self.write({'stage': 'completed'})
        return True

    @api.multi
    def action_cancel(self):
        self.ensure_one()

        self.write({'stage': 'cancelled'})
        return True        