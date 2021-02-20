from odoo import fields, models, api


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _description = "Patient Record"

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Char(string='Age')
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
