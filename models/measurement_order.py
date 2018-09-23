# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.fields import Date

class MeasurementOrder(models.Model):
    _name = 'market.research.measurement.order'
    _description = _("Management of the price analysis process")

    name = fields.Char(string="Name", translate=True)
    responsible_id = fields.Many2one('res.users', string="Responsible User")
    deadline_date = fields.Date(string="Deadline")
    approval_date = fields.Date(string="Approval Date")
    stage = fields.Selection([
            ('draft', 'Draft'), 
	    	('planned', 'Planned'), 
	    	('completed', 'Completed'), 
	    	('cancelled', 'Cancelled')
            ],default='draft')

    tradepoint_order_ids = fields.One2many('market.research.tradepoint.order', 'measurement_order_id', string="Trade Points")
    product_ids = fields.One2many('market.research.product', 'measurement_order_id', string="Products")

    @api.model
    def create(self, vals):
        record = super(MeasurementOrder, self).create(vals)
        
        record.name = _("Measurement order #%d since %s") % (record.id, Date.from_string(record.create_date).strftime("%d.%m.%Y"))

        return record
           
