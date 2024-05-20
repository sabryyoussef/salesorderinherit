# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'almasyia_sales_inherit',
    'version': '1.0',
    'sequence': 190,
    'summary': 'Create and validate approvals requests',
    'description': """

    """,
    'depends': ['mail', 'hr', 'product', 'sale','contacts','base'],
    'data': [
        'sequrity/sequrity.xml',
        'sequrity/ir.model.access.csv',
        'views/res_partner_views.xml',
        'views/construction_project_views.xml',
        'views/statusaddview.xml',
    ],

    'application': True,
    'installable': True,
    'license': 'LGPL-3',
}
