# -*- coding: utf-8 -*-
from odoo import http

# class MicReport(http.Controller):
#     @http.route('/mic_report/mic_report/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mic_report/mic_report/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mic_report.listing', {
#             'root': '/mic_report/mic_report',
#             'objects': http.request.env['mic_report.mic_report'].search([]),
#         })

#     @http.route('/mic_report/mic_report/objects/<model("mic_report.mic_report"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mic_report.object', {
#             'object': obj
#         })