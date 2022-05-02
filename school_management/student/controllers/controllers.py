# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class Student(http.Controller):
    @http.route('/students', type='http', auth='public', website=True)
    def student_list(self, **kw):
        students = request.env['student.student'].sudo().search([])
        return request.render(
            "student.students_list", {
                "students": students,
            })

    @http.route('/students/<model("student.student"):s_id>/', type='http', auth='public', website=True)
    def display_student(self, s_id=0, **kw):
        return request.render(
            'student.student_details', {
                "student": s_id,
            })

    @http.route('/student_form', type='http', auth='user', website=True)
    def student(self, **kw):
        """Function to render form."""
        schools = request.env['school.school'].search([])
        print ("schollsw", schools)
        return request.render('student.create_form', {
            'schools': schools
        })

    @http.route('/student_form/webstudent', type='http', auth='user', website=True)
    def student_webstudent(self, **kw):
        """Function to get & store data in college_management.
        :return: record set"""
        print ("kwwwwwwwwwwwwwww", kw)
        request.env['student.student'].sudo().create(kw)
        # student_list = request.env['student.student'].search([])
        return request.redirect('/students')


#     @http.route('/student/student/objects/<model("student.student"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('student.object', {
#             'object': obj
#         })
