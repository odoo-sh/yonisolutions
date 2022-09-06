# -*- coding: utf-8 -*-
# Copyright 2022 Sodexis
# License OPL-1 (See LICENSE file for full copyright and licensing details).

{
    'name': "Customer Reports",
    'summary': """
        Customized reports for the specific customer.""",
    'version': '15.0.1.0.0',
    'category': 'Uncategorized',
    'website': "http://sodexis.com/",
    'author': "Sodexis",
    'license': 'OPL-1',
    'installable': True,
    'application': False,
    'depends': [
        'base',
        'web',
        'l10n_ch',
    ],
    'data': [
        'views/report_templates.xml',
        'views/report_invoice.xml',
    ],
    'assets': {
        'web.report_assets_common': [
            '/customer_reports/static/src/scss/report_swissqr_custom.scss',
        ],
    },
}
