# -*- coding: utf-8 -*-
from odoo import http

# class MicReportComision(http.Controller):
#     @http.route('/mic_report_comision/mic_report_comision/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mic_report_comision/mic_report_comision/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mic_report_comision.listing', {
#             'root': '/mic_report_comision/mic_report_comision',
#             'objects': http.request.env['mic_report_comision.mic_report_comision'].search([]),
#         })

#     @http.route('/mic_report_comision/mic_report_comision/objects/<model("mic_report_comision.mic_report_comision"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mic_report_comision.object', {
#             'object': obj
#         })