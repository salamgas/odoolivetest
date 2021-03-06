# -*- coding: utf-8 -*-
{
    'name': "pobs_maintenance",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'maintenance'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/report_paperformat.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/new_team_view.xml',
        'views/kanban_view.xml',
        'reports/barcode.xml',
        'reports/barcode_template.xml',
        'reports/barcode_zpl.xml',
        'views/mintenance_issue_view.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
