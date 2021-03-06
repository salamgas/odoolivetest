{
    'name': 'pabs_fawri+_report',
    'category': 'sales',
    'summary': 'Fawri+ Report Customization',
    'version': '1.0',
    'description': """Customization of ticket module as per requirement.""",
    'depends': ['base', 'sale', 'account', 'account_accountant'],
    'data': [
        'data/report_paperformat.xml',
        'views/payments_report.xml',
        'views/cheque_bank_report.xml',
        'reports/fawri+_report_template.xml',
        'reports/fawri_report_template.xml',
        'reports/international_report_template.xml',
        'reports/alsalam_bank_cheque_template.xml',
        'reports/nbk_bank_cheque_template.xml',
        'reports/payment_voucher.xml',
        'views/views.xml',
    ],
    'installable': True,
    'auto_install': False,
}
