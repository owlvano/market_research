from odoo import tools
from odoo import api, fields, models

class PriceReport(models.Model):
    _name = "price.report"
    _description = "Price Measurements Statistics"
    _auto = False
    _rec_name = 'date'
    _order = 'date desc'

    date = fields.Datetime('Create Date', readonly=True)
    measured_price = fields.Float("Measured Price", readonly=True, group_operator='avg')
    measurement_order_id = fields.Many2one('market.research.measurement.order', "Measurement Order", readonly=True)
    client_id = fields.Many2one('res.partner', "Client", readonly=True)
    assigned_user_id = fields.Many2one('res.users', "Assigned User", readonly=True)

    product_id = fields.Many2one('product.product', "Product", readonly=True)

    def _query_price_measurements(self):
        query_str = """
            SELECT
                pm.create_date as date,
                NULLIF(pm.measured_price, 0) as measured_price,
                t.assigned_user_id as assigned_user_id,
                t.client_id as client_id,
                p.id as product_id,
                t.measurement_order_id as measurement_order_id
            FROM (
                market_research_price_measurement pm
                    left join market_research_tradepoint_order t on (pm.tradepoint_order_id=t.id)
                    left join product_product p on (pm.product_id=p.id)
            )
            GROUP BY
                pm.create_date,
                pm.measured_price,
                t.assigned_user_id,
                t.client_id,
                p.id,
                t.measurement_order_id
        """ 
        return query_str
    
    def _query_my_product_prices(self):
        query_str = """
            SELECT
                p.create_date as date,
                NULLIF(p.price, 0) as measured_price,
                m.responsible_id as assigned_user_id,
                m.partner_id as client_id,
                pp.id as product_id,
                m.id as measurement_order_id
            FROM (
                market_research_product p
                    left join market_research_measurement_order m on (p.measurement_order_id=m.id)
                    left join product_product pp on (p.product_id=pp.id)
            )
            GROUP BY 
                    p.create_date,
                    p.price,
                    m.responsible_id,
                    m.partner_id,
                    pp.id,
                    m.id
        """
        return query_str   
    
    @api.model_cr
    def init(self):
        # self._table = price_report
        tools.drop_view_if_exists(self.env.cr, self._table)
        self.env.cr.execute("""CREATE OR REPLACE VIEW %s AS (
            WITH result AS (
                WITH price_measurements AS (
                        %s
                    ), product_prices AS (
                        %s
                    )
                SELECT * FROM price_measurements
                UNION
                SELECT * FROM product_prices
                )
            SELECT row_number() OVER () AS id, * 
            FROM  result
            )
            """ % (self._table, self._query_price_measurements(), self._query_my_product_prices()))

