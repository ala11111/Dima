# -*- coding: utf-8 -*-
# from odoo import http


# class EditCurrentStock(http.Controller):
#     @http.route('/edit_current_stock/edit_current_stock', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edit_current_stock/edit_current_stock/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('edit_current_stock.listing', {
#             'root': '/edit_current_stock/edit_current_stock',
#             'objects': http.request.env['edit_current_stock.edit_current_stock'].search([]),
#         })

#     @http.route('/edit_current_stock/edit_current_stock/objects/<model("edit_current_stock.edit_current_stock"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edit_current_stock.object', {
#             'object': obj
#         })
