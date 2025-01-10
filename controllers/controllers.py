# -*- coding: utf-8 -*-
# from odoo import http


# class Session7(http.Controller):
#     @http.route('/session7/session7', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/session7/session7/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('session7.listing', {
#             'root': '/session7/session7',
#             'objects': http.request.env['session7.session7'].search([]),
#         })

#     @http.route('/session7/session7/objects/<model("session7.session7"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('session7.object', {
#             'object': obj
#         })

