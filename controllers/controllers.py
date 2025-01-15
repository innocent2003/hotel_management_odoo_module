# -*- coding: utf-8 -*-
# from odoo import http


# class SaleSession9(http.Controller):
#     @http.route('/sale_session9/sale_session9', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_session9/sale_session9/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_session9.listing', {
#             'root': '/sale_session9/sale_session9',
#             'objects': http.request.env['sale_session9.sale_session9'].search([]),
#         })

#     @http.route('/sale_session9/sale_session9/objects/<model("sale_session9.sale_session9"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_session9.object', {
#             'object': obj
#         })

