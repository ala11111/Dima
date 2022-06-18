# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StockQuant(models.Model):
    _inherit = "stock.quant"

    image_128 = fields.Image(string="Image",store=False,related='product_id.image_1920')

    @api.onchange('product_id')
    def onchange_sake_product_image(self):
        for product in self:
            product.image_128 = product.product_id.image_1920
