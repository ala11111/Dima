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
        print('xxxxxxxxxxxxxx',debit_account_id)
        print('xxxxxxxxxxxxxx',debit_account_id)
        print('xxxxxxxxxxxxxx',debit_account_id)
        print('xxxxxxxxxxxxxx',debit_account_id)
        account_debit_account=self.env['account.account'].sudo().search([('id','=',debit_account_id)],limit=1)
        print('sssssssssssss',account_debit_account.user_type_id)
        if account_debit_account.user_type_id.id == self.env.ref('account.data_account_type_expenses').id:
            print('fffffffffffffffffffffffffffffffffffffffffffffffff')
            if self.analytic_account_id:

                rslt['debit_line_vals']['analytic_account_id'] = self.analytic_account_id.id
        return rslt







