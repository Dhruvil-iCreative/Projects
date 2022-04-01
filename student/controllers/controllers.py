# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Student(http.Controller):
    @http.route('/students', type='http', auth='public', website=True)
    def index(self, **kw):
        students = request.env['student.student'].sudo().search([])
        return request.render(
            "student.students_list", {
                "students": students
            })

#     @http.route('/student/student/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('student.listing', {
#             'root': '/student/student',
#             'objects': http.request.env['student.student'].search([]),
#         })

#     @http.route('/student/student/objects/<model("student.student"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student.object', {
#             'object': obj
#         })
