# coding=utf-8
from odoo import models, fields, api


class ReportAbonadoWizard(models.TransientModel):
    _name = 'report.abonado.wizard'

    # mes = fields.Selection([('01', 'Enero'), ('02', 'Febrero'), ('03', 'Marzo'), ('04', 'Abril'), ('05', 'Mayo'),
    #                         ('06', 'Junio'), ('07', 'Julio'), ('08', 'Agosto'), ('09', 'Septimiebre'),
    #                         ('10', 'Octubre'), ('11', 'Noviembre'),
    #                         ('12', 'Diciembre')])

    date_from = fields.Date(string='Desde:')
    date_to = fields.Date(string='Hasta:')

    @api.multi
    def print_reportabonado_xls(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'url': '/mic_abonado/models/comision_report?fecha_inicio='+ self.date_from +'&fecha_fin='+ self.date_to+'',
            # 'url': '/reports/report_liquidacioncompra',
            'target': 'new'
        }
