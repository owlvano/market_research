from odoo import tools
from odoo import api, fields, models

class PriceReport(models.Model):
    _name = "price.report"
    _description = "Price Measurements Statistics"
    _auto = False
    _rec_name = 'date'
    _order = 'date desc'

    date = fields.Datetime('Create Date', readonly=True)

    tradepoint_order_id = fields.Many2one('market.research.tradepoint.order', "Tradepoint Order", readonly=True)
    client_id = fields.Many2one('res.partner', "Client", readonly=True)
    assigned_user_id = fields.Many2one('res.users', "Assigned User", readonly=True)

    product_id = fields.Many2one('product.product', "Product", readonly=True)    
    measured_price = fields.Float("Measured Price", readonly=True, group_operator='avg')
    
    price = fields.Float("Own Price", readonly=True, group_operator='avg')

    def _select(self):
        select_str = """
         SELECT pm.id as id,
                pm.measured_price as measured_price,
                pm.create_date as date,
                t.id as tradepoint_order_id,
                t.assigned_user_id as assigned_user_id,
                t.client_id as client_id,
                p.product_id as product_id,
                p.price as price
        """ 
        return select_str

    def _from(self):
        from_str = """
        		market_research_price_measurement pm
        			left join market_research_tradepoint_order t on (pm.tradepoint_order_id=t.id)
                    left join market_research_product p on (pm.product_id=p.product_id)
        """
        return from_str

    def _group_by(self):
        group_by_str = """
           GROUP BY pm.id,
					pm.create_date,
                    pm.measured_price,                    
					t.id,
					t.assigned_user_id,
					t.client_id,
                    p.id,
                    p.price
        """
        return group_by_str

    @api.model_cr
    def init(self):
        # self._table = price_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE or REPLACE VIEW %s as (
            %s
            FROM ( %s )
            %s
            )""" % (self._table, self._select(), self._from(), self._group_by()))
