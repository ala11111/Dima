# -*- coding: utf-8 -*-
# from odoo import http


# class AnalyticAccountScrab(http.Controller):
#     @http.route('/analytic_account_scrab/analytic_account_scrab', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/analytic_account_scrab/analytic_account_scrab/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('analytic_account_scrab.listing', {
#             'root': '/analytic_account_scrab/analytic_account_scrab',
#             'objects': http.request.env['analytic_account_scrab.analytic_account_scrab'].search([]),
#         })

#     @http.route('/analytic_account_scrab/analytic_account_scrab/objects/<model("analytic_account_scrab.analytic_account_scrab"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('analytic_account_scrab.object', {
#             'object': obj
#         })
