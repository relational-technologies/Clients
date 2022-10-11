# -*- encoding: utf-8 -*-

{
    'name': 'Budgetary control',
    'version': '1.0',
    'category': 'Analytic',
    'description': """
This module allows to set budgets between a date interval and related to
analytic accounts, and see their progress easily.
    """,
    'author': 'Serv. Tecnolog. Avanzados - Femi Oloyede',
    'website': 'http://www.serviciosbaeza.com',
    'depends': [
        'account',
    ],
    'data': [
        'views/budgetary_control_view.xml',
        'security/ir.model.access.csv',
        'security/budget_security.xml',
    ],
    "installable": True,
}
