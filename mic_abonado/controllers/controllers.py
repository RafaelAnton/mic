# -*- coding: utf-8 -*-
from odoo import http

# class MicAbonado(http.Controller):
#     @http.route('/mic_abonado/mic_abonado/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mic_abonado/mic_abonado/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mic_abonado.listing', {
#             'root': '/mic_abonado/mic_abonado',
#             'objects': http.request.env['mic_abonado.mic_abonado'].search([]),
#         })

#     @http.route('/mic_abonado/mic_abonado/objects/<model("mic_abonado.mic_abonado"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mic_abonado.object', {
#             'object': obj
#         })