from odoo import fields, models, api, _


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Patient Record"
    _rec_name = "patient_name"

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Char(string='Age')
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string="Patient ID", required=True, copy=False,
                           readonly=True, index=True, default=lambda self: _('New'))
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('fe_male', 'Female'), ], default='male')


    @api.model
    def create(self, vals_list):
        if vals_list.get('name_seq', _('New')):
            vals_list['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals_list)
        return result
