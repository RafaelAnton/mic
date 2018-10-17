# -*- coding: utf-8 -*-
from odoo import tools
from odoo import api, fields, models


class abonado_report(models.Model):
    _name = 'abonado.report'
    _auto = False
    _description = 'reporte de abonado'

    cliente = fields.Char(string=u'Cliente')
    codigo=fields.Char(string=u'Codigo de Suscripción')
    feha_creacion = fields.Date(string="Fecha de Creacion")
    fecha_sucripcion = fields.Date(string="Fecha de Suscripcion")
    fecha_inicio = fields.Date(string='Fecha de Inicio')
    abonado = fields.Float(string="Abonado")
    abonado_rtv = fields.Float(string="Abonado RTVE")

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'abonado_report')
        self._cr.execute("""
    CREATE OR REPLACE VIEW abonado_report AS 
        SELECT
    anali.id as id,
    anali.name as codigo,
    res.name as cliente,
    to_char(sus.create_date,'DD-MM-YYYY') as feha_creacion,
    sus.date as fecha_sucripcion,
    sus.date_start as fecha_inicio,
    sus.abonado as abonado,
    susline.abonado as abonado_rtv
    FROM sale_subscription_line susline
    inner join sale_subscription sus on sus.analytic_account_id=susline.analytic_account_id
    inner join account_analytic_account anali on susline.analytic_account_id=anali.id
    inner join res_partner res on res.id=anali.partner_id;""")


