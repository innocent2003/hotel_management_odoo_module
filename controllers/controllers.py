# -*- coding: utf-8 -*-
# from odoo import http


# class AdminHotel(http.Controller):
#     @http.route('/admin_hotel/admin_hotel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/admin_hotel/admin_hotel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('admin_hotel.listing', {
#             'root': '/admin_hotel/admin_hotel',
#             'objects': http.request.env['admin_hotel.admin_hotel'].search([]),
#         })

#     @http.route('/admin_hotel/admin_hotel/objects/<model("admin_hotel.admin_hotel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('admin_hotel.object', {
#             'object': obj
#         })

