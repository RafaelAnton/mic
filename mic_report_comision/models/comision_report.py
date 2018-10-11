# -*- coding: utf-8 -*-
from odoo import tools
from odoo import api, fields, models


class comision_report(models.Model):
    _name = 'suscription.comision.report'
    _auto = False
    _description = 'reporte de comisones'

    senial = fields.Char(string=u'Señal')
    nombre_Cliente = fields.Char(string="Cliente")
    numero_de_factura = fields.Char(string="Numero De  Factura")
    factumatri=fields.Char(string='Factura Matriz')
    fehca_de_factura = fields.Date(string="Fecha de Pago")
    monto = fields.Float(string="Monto de la Factura")
    comision_pocentaje = fields.Float(string=u"Porcentaje de Comisión")
    monto_de_comision = fields.Float(string=u"Monto de Comsión")

    @api.model_cr
    def init(self):
        tools.drop_view_if_exists(self._cr, 'suscription_comision_report')
        self._cr.execute("""
CREATE OR REPLACE VIEW suscription_comision_report AS 
                select 
  inv.id as id,
  template2.name as senial,
  resp.name      as nombre_Cliente,
  inv.number     as numero_de_factura,
  inv.factura_matriz as factumatri,
  inv.date       as fehca_de_factura,
  inv.amount_total as monto,
  template2.porcentaje_interes as comision_pocentaje,
  sus.comision as monto_de_comision

from
  account_analytic_account analy
  inner join sale_subscription sus on analy.id = sus.analytic_account_id
  inner join account_invoice_line inv_line on sus.id = inv_line.account_analytic_id
  inner join account_invoice inv on inv_line.invoice_id = inv.id
  inner join mic_cabecera m2 on sus.cabecera_id = m2.id
  inner join res_partner resp on analy.partner_id = resp.id
  inner join product_product product on m2.signal_id = product.id
  inner join product_template template2 on product.product_tmpl_id = template2.id
where inv.state = 'paid';
                """)
