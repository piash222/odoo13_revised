from odoo import api, models, _


class PatientCardReport(models.AbstractModel):
    _name = 'report.om_hospital.report_patient'
    _description = "Patient Card Report"

    def _get_report_values(self, docids, data=None):
        docs = self.env['hospital.patient'].browse(docids[0])
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        appointment_list = []
        for appointment in appointments:
            vals = {
                'name': appointment.patient_id,
                'notes': appointment.notes,
                'appointment_date': appointment.appointment_date
            }
            appointment_list.append(vals)

        return {
            'docs': docs,
            'appointment_list': appointment_list
        }
