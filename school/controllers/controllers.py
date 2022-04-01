#-*- coding: utf-8 -*-
# from odoo import http
# from odoo.http import request
#
#
# class School(http.Controller):
#     @http.route('/school', type='http', auth='public', website=True)
#     def index(self, **kw):
#         schools = request.env['school.school'].sudo().search([])
#         return request.render(
#             "school.school_list", {
#                 "schools": schools
#             })
#     @http.route('/school/school/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('school.listing', {
#             'root': '/school/school',
#             'objects': http.request.env['school.school'].search([]),
#         })

#     @http.route('/school/school/objects/<model("school.school"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school.object', {
#             'object': obj
#         })
