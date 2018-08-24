# -*- coding: utf-8 -*-
from odoo import http

# class MicEquipos(http.Controller):
#     @http.route('/mic_equipos/mic_equipos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mic_equipos/mic_equipos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mic_equipos.listing', {
#             'root': '/mic_equipos/mic_equipos',
#             'objects': http.request.env['mic_equipos.mic_equipos'].search([]),
#         })

#     @http.route('/mic_equipos/mic_equipos/objects/<model("mic_equipos.mic_equipos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mic_equipos.object', {
#             'object': obj
#         })