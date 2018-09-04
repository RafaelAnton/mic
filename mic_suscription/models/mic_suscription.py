# coding=utf-8
from odoo import api, models, fields


class SucriptionMic(models.Model):
    _inherit = 'sale.subscription'

    cabecera_id = fields.Many2one('mic.cabecera', string=u"Señal")
    cabecera_partner = fields.Many2one('res.partner', related="cabecera_id.partner_id")
    cabecera_equipo = fields.Many2one('product.product', related="cabecera_id.equipo_id")
    cabecera_cabecera = fields.Char(related="cabecera_id.cabecera")

    cabecera_caracteristicas = fields.One2many('mic.caracteristica.equipos',
                                               related="cabecera_id.equipo_caracteristica")
    cabecera_estado = fields.Selection(related="cabecera_id.estado")
    cabecera_motivo = fields.Selection(related="cabecera_id.motivo")
    comision = fields.Float(compute='compute_comision_sucription', string="Comision", store=True,
                            track_visibility='onchange')

