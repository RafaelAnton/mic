# -*- coding: utf-8 -*-
from odoo import http

# class MicFactura(http.Controller):
#     @http.route('/mic_factura/mic_factura/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mic_factura/mic_factura/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mic_factura.listing', {
#             'root': '/mic_factura/mic_factura',
#             'objects': http.request.env['mic_factura.mic_factura'].search([]),
#         })

#     @http.route('/mic_factura/mic_factura/objects/<model("mic_factura.mic_factura"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mic_factura.object', {
#             'object': obj
#         })