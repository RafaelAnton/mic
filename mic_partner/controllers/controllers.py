# -*- coding: utf-8 -*-
from odoo import http

# class MicPartner(http.Controller):
#     @http.route('/mic_partner/mic_partner/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/mic_partner/mic_partner/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('mic_partner.listing', {
#             'root': '/mic_partner/mic_partner',
#             'objects': http.request.env['mic_partner.mic_partner'].search([]),
#         })

#     @http.route('/mic_partner/mic_partner/objects/<model("mic_partner.mic_partner"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('mic_partner.object', {
#             'object': obj
#         })