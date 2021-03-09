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
