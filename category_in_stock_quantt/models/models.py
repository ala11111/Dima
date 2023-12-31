# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class StockQuant(models.Model):
    _inherit = 'stock.quant'

    categ_id = fields.Many2one(comodel_name="product.category", string="Category", required=False,related='product_id.categ_id',store=True )




class StockMove(models.Model):
    _inherit = 'stock.move'

    categ_id = fields.Many2one(comodel_name="product.category", string="Category 1", required=False,related='product_id.categ_id',store=True )


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    categ_id = fields.Many2one(comodel_name="product.category", string="Category 2", required=False,related='product_id.categ_id',store=True )


#
# class StockValuationLayer(models.Model):
#     _inherit = 'stock.valuation.layer'
#
#     categ_id = fields.Many2one(comodel_name="product.category", string="Category", required=False,related='product_id.categ_id',store=True )
#
#
# #
# class ReportStockQuantity(models.Model):
#     _inherit = 'report.stock.quantity'
#
#     categ_id = fields.Many2one(comodel_name="product.category", string="Category", required=False,related='product_id.categ_id',store=True )
#
