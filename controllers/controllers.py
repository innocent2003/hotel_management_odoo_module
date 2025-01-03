# -*- coding: utf-8 -*-
# from odoo import http


# class InheritHotel(http.Controller):
#     @http.route('/inherit_hotel/inherit_hotel', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inherit_hotel/inherit_hotel/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('inherit_hotel.listing', {
#             'root': '/inherit_hotel/inherit_hotel',
#             'objects': http.request.env['inherit_hotel.inherit_hotel'].search([]),
#         })

#     @http.route('/inherit_hotel/inherit_hotel/objects/<model("inherit_hotel.inherit_hotel"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inherit_hotel.object', {
#             'object': obj
#         })

