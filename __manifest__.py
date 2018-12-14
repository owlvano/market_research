# -*- coding: utf-8 -*-
{
    'name': "Market Research",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Ivan Sova",
    'website': "http://www.odoobudo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'application': True,
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        # 'security/user_groups.xml',
        'security/ir.model.access.csv',
        'wizard/price_report_wizard_views.xml',
        'report/price_report_views.xml',
        'views/market_research_views.xml',
        'views/measurement_order_views.xml',
        'views/product_views.xml',
        'views/price_measurement_views.xml',
        'views/tradepoint_order_views.xml',
        'views/market_research_views_technical.xml',
        'views/sale_views.xml',
    ],

}
