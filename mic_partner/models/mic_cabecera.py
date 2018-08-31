# -*- coding: utf-8 -*-
from odoo import models, fields


class MicPartnerEquipo(models.Model):
    _name = "mic.cabecera"

    signal_id = fields.Many2one('product.product', string=u"Señal", required=True)
    equipo_id = fields.Many2one('product.product', string="Equipo", required=True)
    partner_id = fields.Many2one('res.partner', string="Nombre Cliente", required=True)
    cabecera = fields.Char(String='Direccion')
    estado = fields.Selection([('activo', 'Activo'), ('inactivo', 'Inactivo')], 'Estado', default='activo',
                              required=True)
    motivo = fields.Selection(
        [('finaliza', 'Finaliza Contrato'), ('deuda', 'Deuda'), ('equipomal', 'Equipo Malogrado'),
         ('problema', 'Problema Tecnico'), ('solicitud', 'Solicitud Cliente')],
        'Motivo')
    equipo_caracteristica = fields.One2many('mic.caracteristica.equipos',related="equipo_id.caracteristica_ids")


