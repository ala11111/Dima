# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockQuant(models.Model):
    _inherit = "stock.quant"

    image_128 = fields.Image(string="Image",store=False,related='product_id.image_1920')
    value_sale = fields.Float(string="Value2",  required=False,compute='get_value_sale',store=True )


    @api.depends('available_quantity','product_id','product_id.list_price')
    def get_value_sale(self):
        for rec in self:
            if rec.available_quantity > 0 :
                rec.value_sale = rec.available_quantity * rec.product_id.list_price
            else:
                rec.value_sale = rec.value_sale

    @api.onchange('product_id')
    def onchange_sake_product_image(self):
        for product in self:
            product.image_128 = product.product_id.image_1920
