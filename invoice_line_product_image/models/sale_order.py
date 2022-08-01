# -*- coding: utf-8 -*-
# Part of Browseinfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models,_

class AccountMoveLine(models.Model):
    _inherit = "account.move.line"

    image_128 = fields.Image(string="Image",related='product_id.image_1920')

    @api.onchange('product_id')
    def onchange_sake_product_image(self):
    	for product in self:
    		product.image_128 = product.product_id.image_1920


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    image_128 = fields.Image(string="Image",related='product_id.image_1920')

    @api.onchange('product_id')
    def onchange_sake_product_image(self):
    	for product in self:
    		product.image_128 = product.product_id.image_1920
