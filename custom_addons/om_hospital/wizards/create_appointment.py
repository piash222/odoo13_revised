from odoo import models, fields, api, _


class CreateAppointment(models.TransientModel):
    _name = 'create.appointment'

    patient_id = fields.Many2one('hospital.patient', string="patient")
    appointment_date = fields.Date(string="appointment Date")

    def create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'patient_age': self.patient_id.patient_age,
            'notes': "created from menu",
            'appointment_date': self.appointment_date
        }
        self.env['hospital.appointment'].create(vals)

    def print_report(self):
        print(self.read()[0])
        data = {
            'model': "create.appointment",
            'form': self.read()[0]
        }
        # selected_patient = data['form']['patient_id'][0]
        # appointments = self.env['hospital.appointment'].search([('patient_id', '=', selected_patient)])

        # data['appointments'] = appointments
        print(data)
        return self.env.ref('om_hospital.report_appointment').report_action(self, data=data)
