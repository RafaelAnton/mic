# -*- coding: utf-8 -*-
from odoo import models, fields, api


class MicEquipoCaracteristicas(models.Model):
    _name = "mic.caracteristica.equipos"

    product_id = fields.Many2one('product.product', string="Nombre Producto", required=True)
    caracteristica_id = fields.Many2one('mic.caracteristica', string="Nombre de dato Asociado", required=True)
    numero = fields.Char(string="Numero Serie De Datos Asociado")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            name = "%s: %s" % (record.caracteristica_id.caracteristica_nombre, record.numero)
            result.append((record.id, name))
        return result
