# coding=utf-8
from StringIO import StringIO

from datetime import datetime

import xlsxwriter

from odoo import http
from odoo.http import request


class ReportGestionController(http.Controller):
    @http.route('/mic_abonado/models/comision_report', type='http', auth="user")
    def index(self, fecha_inicio, fecha_fin, **kw):
        gestion_lines = request.env['abonado.report'].search([('fecha_sucripcion', '>=', fecha_inicio),
                                                              ('fecha_sucripcion', '<=', fecha_fin)])
        if len(gestion_lines) == 0:
            return "<h3>No existen datos para el reporte</h3>"
        else:
            return self.render_excel(gestion_lines)

    def render_excel(self, datos):
        if len(datos):
            excel = StringIO()
            workbook = xlsxwriter.Workbook(excel)

            header = workbook.add_format()
            header.pattern = 1
            header.set_bg_color('#C1C0BB')
            header.set_bold(True)
            header.set_border()

            title = workbook.add_format()
            title.set_bold()
            title.set_font_size(14)

            body = workbook.add_format()
            body.set_border()

            hoja = workbook.add_worksheet(u'Reporte de abonado')

            hoja.write_row(1, 1,
                           (u'STAND / # REFERENCIA DE SUSCRIPCIÓN',
                            u'NOMBRE CLIENTE',
                            u'FECHA DE CREACIÓN',
                            u'FECHA DE SUSCRIPCION',
                            u'FECHA DE INICIO',
                            u'ABONADO',
                            u'ABONADO RTVE'), header)

            row_idx = 2
            for dato in datos:
                hoja.write_row(row_idx, 1, (
                    dato.codigo,
                    dato.cliente,
                    dato.feha_creacion,
                    dato.fecha_sucripcion,
                    dato.fecha_inicio,
                    dato.abonado,
                    dato.abonado_rtv
                ), body)
                row_idx += 1

            workbook.close()

            response = request.make_response(excel.getvalue(),
                                             headers=[('Content-Type', 'application/vnd.ms-excel'),
                                                      ('Content-Disposition',
                                                       'attachment; filename=RPT_ABONADOS%s.xlsx;' %
                                                       datetime.now().strftime('%Y-%m-%d'))])
            excel.close()

            return response
