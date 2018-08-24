# -*- coding: utf-8 -*-
from odoo import models, fields


class MicEquipoCaracteristicas(models.Model):
    _name = "mic.caracteristica.equipos"
    producto_id = fields.Many2one('product.product', string="Nombre Producto", required=True)
    caracteristica_id = fields.Many2one('mic.caracteristica', string="Nombre de dato Asociado", required=True)
    numero=fields.Float(string="Numero Serie De Datos Asociado")
