# -*- coding: utf-8 -*-
from odoo import http

# class MicSuscription(http.Controller):
#     @http.route('/mic_suscription/mic_suscription/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mic_suscription/mic_suscription/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mic_suscription.listing', {
#             'root': '/mic_suscription/mic_suscription',
#             'objects': http.request.env['mic_suscription.mic_suscription'].search([]),
#         })

#     @http.route('/mic_suscription/mic_suscription/objects/<model("mic_suscription.mic_suscription"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mic_suscription.object', {
#             'object': obj
#         })