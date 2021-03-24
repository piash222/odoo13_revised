from odoo import api, models


class PatientCardReport(models.AbstractModel):
    _name = 'report.om_hospital.report_patient'
    _description = 'Patient Card Description'

    @api.model
    def _get_report_values(self, docids, data=None):
        print(docids)

        docs = self.env['hospital.patient'].browse(docids[0])
        appointments = self.env['hospital.appointment'].search([('patient_id', '=', docids[0])])
        print(appointments)
        appointment_list = []
        for appointment in appointments:
            vals = {
                'name': appointment.patient_id.patient_name,
                'notes': appointment.notes,
                'appointment_date': appointment.appointment_date
            }
            appointment_list.append(vals)
        print(appointment_list)
        return {
            'docs': docs,
            'appointment_list': appointment_list
        }
