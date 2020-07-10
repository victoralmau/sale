# -*- coding: utf-8 -*-
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
{
    'name': 'Cashondelivery',
    'version': '10.0.1.0.0',    
    'author': 'Odoo Nodriza Tech (ONT)',
    'website': 'https://nodrizatech.com/',
    'category': 'Tools',
    'license': 'AGPL-3',
    'depends': ['base', 'sale', 'stock', 'account'],
    'data': [
        'views/account_payment_mode_view.xml',
        'views/sale_order_view.xml',
        'views/stock_picking_view.xml',
    ],
    'installable': True,
    'auto_install': False,    
}