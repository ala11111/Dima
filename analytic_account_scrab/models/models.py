# -*- coding: utf-8 -*-

from odoo import models, fields, api

class StockScrap(models.Model):
    _inherit = 'stock.scrap'

    is_analytic = fields.Boolean(string="Analytic",  )
    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account")


    def _prepare_move_values(self):
        vals = super(StockScrap, self)._prepare_move_values()
        if self.analytic_account_id:
            vals['analytic_account_id'] = self.analytic_account_id.id
        return vals





class StockMoveInherit(models.Model):
    _inherit = 'stock.move'


    analytic_account_id = fields.Many2one('account.analytic.account', string="Analytic Account")
    is_analytic = fields.Boolean(string="", )

    def _generate_valuation_lines_data(self, partner_id, qty, debit_value, credit_value, debit_account_id, credit_account_id, description):
        """ Overridden from stock_account to support amount_currency on valuation lines generated from po
        """
        self.ensure_one()

        rslt = super(StockMoveInherit, self)._generate_valuation_lines_data(partner_id, qty, debit_value, credit_value, debit_account_id, credit_account_id, description)
        if self.analytic_account_id:

            rslt['debit_line_vals']['analytic_account_id'] = self.analytic_account_id.id
        return rslt







