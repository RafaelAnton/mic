# -*- coding: utf-8 -*-
from odoo import api, models, fields
import requests
import bs4


class EquipoMic(models.Model):
    _inherit = 'product.template'
    tipo_equipo = fields.Selection([('equipo', 'Equipo'), ('signal', u'Señal'), ('otros', 'Otros')], required=True,
                                   store=True,
                                   index=True, default='otros')

    signal_ids = fields.Many2many('product.product', string='Señal Asignada')

    caracteristica_ids = fields.One2many('mic.caracteristica.equipos', 'product_id')

    porcentaje_interes = fields.Float(string=u'Porcentaje de Comisión %')
