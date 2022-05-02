# -*- coding: utf-8 -*-
{
    'name': "Rental Management",

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'product', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        "views/rental_management_views.xml",
        "views/rental_type_views.xml",
        "views/updated_product_views.xml",
        "wizard/rental_type_wiz_views.xml",
        "views/menu.xml",
    ],

}
