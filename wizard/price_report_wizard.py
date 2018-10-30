from odoo import api, fields, models
from odoo.fields import Date

class PriceReportWizard(models.TransientModel):
    _name = "price.report.wizard"
    _description = "Price Report Wizard"

    product_id = fields.Many2one('product.product', "Product")
    date_from = fields.Date('Date From')
    date_to = fields.Date('Date To')

    def format_date(self, raw_date):
        return Date.from_string(raw_date).strftime("%d.%m.%Y")
        
    @api.multi
    def do_search(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_window',
            'name': 'Price Report (%s - %s)' % (self.format_date(self.date_from), self.format_date(self.date_to)), 
            'res_model': 'price.report',
            'view_mode': 'graph',
            'context': {'group_by': ['date:day','client_id'], 'search_default_product_id': self.product_id.id},
            'domain': ['&',
                ('date','>=', self.date_from),
                ('date','<=', self.date_to)],
            'target': 'main'
        }
