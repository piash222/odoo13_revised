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
        self.patient_id.message_post(body="Appointment Created Successfully", subject="Appointment Creation")
        self.env['hospital.appointment'].create(vals)

    def get_data(self):
        print("getting data")
        appointments = self.env["hospital.appointment"].search([('patient_id', '=', self.patient_id.id)])
        for rec in appointments:
            print(rec.name)
        return {
            "type": "ir.actions.do_nothing"
        }

    def delete_patient(self):
        for rec in self:
            rec.patient_id.unlink()
            
    def print_report(self):
        data = {
            'model': 'create.appointment',
            'form': self.read()[0],

        }
        # if self.read()[0]['patient_id']:
        #     selected_patient = self.read()[0]['patient_id'][0]
        #     appointments = self.env['hospital.appointment'].search([('patient_id', '=', selected_patient)])
        # else:
        #     appointments = self.env['hospital.appointment'].search([])
        # print(appointments)
        # appointment_list = []
        #
        # for appointment in appointments:
        #     vals = {
        #         'name': appointment.patient_id.patient_name,
        #         'notes': appointment.notes,
        #         'appointment_date': appointment.appointment_date
        #     }
        #     appointment_list.append(vals)
        # print(appointment_list)
        #
        # data['appointments'] =  appointment_list
        print('data', data)
        return self.env.ref('om_hospital.report_appointment').report_action(self, data=data)
