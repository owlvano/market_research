# -*- coding: utf-8 -*-
from odoo import http

# class MarketResearch(http.Controller):
#     @http.route('/market_research/market_research/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/market_research/market_research/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('market_research.listing', {
#             'root': '/market_research/market_research',
#             'objects': http.request.env['market_research.market_research'].search([]),
#         })

#     @http.route('/market_research/market_research/objects/<model("market_research.market_research"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('market_research.object', {
#             'object': obj
#         })