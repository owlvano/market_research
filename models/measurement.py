# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Measurement(models.Model):
    _name = 'market_research.measurement'
	_description = u"Хранение данных о ходе проведения замера в конкретной точке"

    order_id = fields.Many2one('market_research.measuring.order', string="Measuring Order")
    client_id = fields.Many2one('res.partner', string="Client")
    assigned_user_id = fields.Many2one('res.users', string="Assigned User")
    end_date = fields.Datetime(string="Measurement End Date")
