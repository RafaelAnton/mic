# coding=utf-8


from odoo import api, models, fields


class FacturaMic(models.Model):
    _inherit = 'account.invoice'

    factura_matriz = fields.Float(string=u'N°Factura Matriz')


