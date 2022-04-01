# -*- coding: utf-8 -*-
# from odoo import http


# class Every(http.Controller):
#     @http.route('/every/every', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/every/every/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('every.listing', {
#             'root': '/every/every',
#             'objects': http.request.env['every.every'].search([]),
#         })

#     @http.route('/every/every/objects/<model("every.every"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('every.object', {
#             'object': obj
#         })
