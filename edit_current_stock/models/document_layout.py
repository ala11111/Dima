from odoo import api, fields, models


class BaseDocumentLayout(models.TransientModel):
    _inherit = 'base.document.layout'

    street = fields.Char(related="company_id.street")
    street2 = fields.Char(related="company_id.street2")


