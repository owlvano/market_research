# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp

class MeasurementOrder(models.Model):
    _name = 'market_research.measurement.order'
    _description = u"Управление процессом проведения анализа цен"

    name = fields.Char()
    responsible_id = fields.Many2one('res.users', string="Responsible User")
    deadline_date = fields.Date(string="Deadline")
    approval_date = fields.Date(string="Approval Date")
    stage = fields.Selection([
            ('draft', u'Draft'), 
	    	('planned', u'Planned'), 
	    	('completed', u'Completed'), 
	    	('cancelled', u'Cancelled')
            ],default='draft')

    tradepoint_order_ids = fields.One2many('market_research.tradepoint.order', 'measurement_order_id', string="Tradepoint Orders")
    product_ids = fields.One2many('market_research.product', 'measurement_order_id', string="Measurable Products")

class TradepointOrder(models.Model):
    _name = 'market_research.tradepoint.order'
    _description = u"Хранение данных о ходе проведения замера в конкретной точке"

    client_id = fields.Many2one('res.partner', string="Client")
    assigned_user_id = fields.Many2one('res.users', string="Assigned User")
    deadline_date = fields.Datetime(string="Deadline")

    measurement_order_id = fields.Many2one('market_research.measurement.order', string="Measurement Order")

class Product(models.Model):
    _name = 'market_research.product'
    _description = u"Хранение данных о перечне товаров, по которым планируется проведение замера цен"

    product_id = fields.Many2one('product.product', string="Product")
    price = fields.Float(string="Price", digits=dp.get_precision('Product Price'))

    measurement_order_id = fields.Many2one('market_research.measurement.order', string="Measurement Order")