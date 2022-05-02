{
    'name': "Inheritance",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'contacts', 'product', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizard/employee_timesheet_reporting.xml',
        'views/account_move_views.xml',
        'views/account_move_line_views.xml',
        'views/inherit_views.xml',
        'views/contact_improve_views.xml',
        'views/settings_config.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'license': "LGPL-3"
}
