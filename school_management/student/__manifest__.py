# -*- coding: utf-8 -*-
{
    'name': "student",

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
    'depends': ['base', 'school', 'mail', 'website'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/mail_template.xml',
        'views/student_views.xml',
        'views/appointments_views.xml',
        'views/professor_views.xml',
        'views/tasks_views.xml',
        'views/students_list.xml',
        'views/menu.xml',
        'views/website_form.xml',
        'reports/paper_format_student_report.xml',
        'reports/report_templates.xml',
        'reports/report.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'student/static/src/css/student_form.css',
        ],
    },
        # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
