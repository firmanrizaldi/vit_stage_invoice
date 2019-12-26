# -*- coding: utf-8 -*-
{
    'name': "vit_stage_invoice",

    'summary': """
        - Menambahkan field stages di account.invoice
        - Manambahkan group by stages 
        """,

    'description': """
        Long description of module's purpose
    """,

    
    'author': 'firmanrizaldiyusup@gmail.com',
    'website': 'http://www.vitraining.com',

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'views/views.xml',
        'data/vit_stage_invoice.stage.csv',
        'security/ir.model.access.csv',
    ],
  
}