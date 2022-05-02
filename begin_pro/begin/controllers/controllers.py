# -*- coding: utf-8 -*-
# from odoo import http


# class Begin(http.Controller):
#     @http.route('/begin/begin', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/begin/begin/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('begin.listing', {
#             'root': '/begin/begin',
#             'objects': http.request.env['begin.begin'].search([]),
#         })

#     @http.route('/begin/begin/objects/<model("begin.begin"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('begin.object', {
#             'object': obj
#         })
