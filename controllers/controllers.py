# -*- coding: utf-8 -*-
# from odoo import http


# class HotelInvoice(http.Controller):
#     @http.route('/hotel_invoice/hotel_invoice', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotel_invoice/hotel_invoice/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotel_invoice.listing', {
#             'root': '/hotel_invoice/hotel_invoice',
#             'objects': http.request.env['hotel_invoice.hotel_invoice'].search([]),
#         })

#     @http.route('/hotel_invoice/hotel_invoice/objects/<model("hotel_invoice.hotel_invoice"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotel_invoice.object', {
#             'object': obj
#         })

