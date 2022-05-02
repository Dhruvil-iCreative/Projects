from odoo import http, _
from odoo.http import request


class Website(http.Controller):
    """Class for Website Controller."""

    # @http.route('/student_form', type='http', auth='user', website=True)
    # def student(self, **kw):
    #     """Function to render form."""
    #     schools = request.env['school.school'].search([])
    #     return request.render('create_form', {
    #         'schools': schools
    #     })
    #
    # @http.route('/student_form/webstudent', type='http', auth='user', website=True)
    # def student_webstudent(self, **kw):
    #     """Function to get & store data in college_management.
    #     :return: record set"""
    #     request.env['student.student'].sudo().create(kw)
    #     # student_list = request.env['student.student'].search([])
    #     return request.render('student.students_list', {})
