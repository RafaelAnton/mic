# coding=utf-8
from odoo import api, models, fields


class ClienteMic(models.Model):
    _inherit = 'res.partner'

    retencion = fields.Float(u'Retención %')
    sidsa = fields.Char(u'RTVE NRO CLIENTE')
    abonado = fields.Boolean(u'Abonado', default=True)
    cabecera_ids = fields.One2many('mic.cabecera', 'partner_id')
