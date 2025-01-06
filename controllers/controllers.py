# -*- coding: utf-8 -*-
# from odoo import http


# class AdminRole(http.Controller):
#     @http.route('/admin_role/admin_role', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/admin_role/admin_role/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('admin_role.listing', {
#             'root': '/admin_role/admin_role',
#             'objects': http.request.env['admin_role.admin_role'].search([]),
#         })

#     @http.route('/admin_role/admin_role/objects/<model("admin_role.admin_role"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('admin_role.object', {
#             'object': obj
#         })

