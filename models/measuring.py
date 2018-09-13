# -*- coding: utf-8 -*-

from odoo import models, fields, api
import odoo.addons.decimal_precision as dp

class MeasuringOrder(models.Model):
    _name = 'market_research.measuring.order'
	_description = u"Управление процессом проведения анализа цен"

    responsible_id = fields.Many2one('res.users', string="Responsible User")
    deadline_date = fields.Date(string="Deadline")
    approval_date = fields.Date(string="Approval Date")
    state = fields.Selection([('draft', u'Черновик'), 
					    	('planned', u'Запланировано'), 
					    	('completed', u'Выполнен'), 
					    	('cancelled', u'Отменено')])

class MeasuringProduct(models.Model):
    _name = 'market_research.measuring.product'
	_description = u"Хранение данных о перечне товаров, по которым планируется проведение замера цен"

    order_id = fields.Many2one('market_research.measuring.order', string="Measuring Order")
    product_id = fields.Many2one('product.product', string="Product")

class MeasuringItem(models.Model):
    _name = 'market_research.measuring.item'
	_description = u"Хранение данных о перечне товаров, по которым планируется проведение замера цен"

    measurement_id = fields.Many2one('market_research.measurement', string="Measurement")
    measuring_product_id = fields.Many2one('market_research.measuring.product', string="Measuring Product")
    
    order_id = fields.Many2one('market_research.measuring.order', string="Measuring Order")
    client_id = fields.Many2one('res.partner', string="Client")
    product_id = fields.Many2one('product.product', string="Product")
	price = fields.Float(string="Price", digits=dp.get_precision('Product Price'))