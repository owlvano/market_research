# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.fields import Datetime

class MeasurementOrder(models.Model):
    _name = 'market_research.measurement.order'
    _description = _("Management of the price analysis process")

    name = fields.Char(compute='_compute_name', store=True, translate=True)
    summary = fields.Char()
    responsible_id = fields.Many2one('res.users', string="Responsible User")
    deadline_date = fields.Date(string="Deadline")
    approval_date = fields.Date(string="Approval Date")
    stage = fields.Selection([
            ('draft', u'Draft'), 
	    	('planned', u'Planned'), 
	    	('completed', u'Completed'), 
	    	('cancelled', u'Cancelled')
            ],default='draft')

    tradepoint_order_ids = fields.One2many('market_research.tradepoint.order', 'measurement_order_id', string="Trade Points")
    product_ids = fields.One2many('market_research.product', 'measurement_order_id', string="Products")

    @api.multi
    @api.depends('create_date')
    def _compute_name(self):
        if self.create_date:
            self.name = _("Measurement order #%d since %s") % (self.id, Datetime.from_string(self.create_date).strftime("%d.%m.%Y"))
