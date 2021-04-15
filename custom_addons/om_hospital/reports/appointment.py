from odoo import api, models


class PatientCardReport(models.AbstractModel):
    _name = 'report.om_hospital.report_appointment_tmp'
    _description = 'Patient Appointment Description'

    @api.model
    def _get_report_values(self, docids, data=None):
        print(docids)
        print(data)
        if docids:
            selected_id = docids[0]
            appointments = self.env['hospital.appointment'].search([('id', '=', selected_id)])
        elif data['form']['patient_id']:
            selected_patient = data['form']['patient_id'][0]
            print(data['form']['patient_id'][0])
            appointments = self.env['hospital.appointment'].search([('patient_id', '=', selected_patient)])
        else:
            appointments = self.env['hospital.appointment'].search([])
        appointment_list = []
        for appointment in appointments:
            val = {
                'name': appointment.patient_id.patient_name,
                'notes': appointment.notes,
                'appointment_date': appointment.appointment_date
            }
            appointment_list.append(val)

        return {
            'appointments': appointment_list
        }
