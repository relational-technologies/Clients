# -*- encoding: utf-8 -*-

from openerp import models, fields


class AccountAnalyticAccount(models.Model):
    _inherit = 'account.analytic.account'

    analytic_lines = fields.One2many(
        'account.analytic.line', 'account_id', string='Analytic lines')
