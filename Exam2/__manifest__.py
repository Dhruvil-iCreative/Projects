{
    'name': "Exam2",

    'author': "Dhruvil",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/sale_order_create.xml',
        'views/settings_config.xml',
        'views/contact_improve_views.xml',
        'views/inherit_views.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license': "LGPL-3",
    'application': True,
    'sequence': 12,
    'installable': True,
}
