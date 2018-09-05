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
    comision = fields.Float(computed='compute_comision_sucription', string="Comision", store=True,
                            track_visibility='onchange')

    @api.onchange('cabecera_id')
    def onchange_cabecera_id(self):
        for suscription in self:
            suscription.recurring_invoice_line_ids = [(0, False, {
                u'product_id': suscription.cabecera_id.signal_id.id,
                u'name': suscription.cabecera_id.signal_id.name,
                u'actual_quantity': 1,
                u'quantity': 1,
                u'sold_quantity': 1,
                u'price_unit': suscription.cabecera_id.signal_id.list_price
            })]

    @api.depends('recurring_total')
    def compute_comision_sucription(self):
        for suscription in self:
            comision = ((
                        suscription.recurring_total - suscription.partner_id.retencion)) * suscription.cabecera_id.signal_id.porcentaje_interes
            suscription.comision = comision
