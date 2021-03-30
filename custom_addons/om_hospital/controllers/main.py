from odoo import http
from odoo.http import request


class Hospital(http.Controller):
    # Sample Controller Created
    @http.route('/hospital/patient/', website=True, auth='public')
    def hospital_patient(self, **kwargs):
        # return 'hello world'
        patients = request.env['hospital.patient'].sudo().search([])
        return request.render("om_hospital.patient_page", {
            'patients': patients
        })
