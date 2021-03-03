from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = 'hospital.patient'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Patient Record"
    _rec_name = "patient_name"
    _order = "id desc"

    patient_name = fields.Char(string='Name', required=True)
    patient_age = fields.Integer(string='Age')
    notes = fields.Text(string="Notes")
    image = fields.Binary(string="Image")
    name_seq = fields.Char(string="Patient ID", required=True, copy=False,
                           readonly=True, index=True, default=lambda self: _('New'))
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('fe_male', 'Female'), ], default='male')
    age_group = fields.Selection(
        string='Age Group',
        selection=[('major', 'Major'),
                   ('minor', 'Minor')], compute='set_age_group')
    doctor = fields.Many2one(comodel_name="hospital.doctor", string="Doctor")
    appointment_count = fields.Integer(string="Appointment", compute='get_appointment_count')
    active = fields.Boolean("Active", default=True)

    @api.model
    def create(self, vals_list):
        if vals_list.get('name_seq', _('New')):
            vals_list['name_seq'] = self.env['ir.sequence'].next_by_code('hospital.patient.sequence') or _('New')
        result = super(HospitalPatient, self).create(vals_list)
        return result

    @api.depends('patient_age')
    def set_age_group(self):
        for rec in self:
            if rec.patient_age < 18:
                rec.age_group = 'minor'
            else:
                rec.age_group = "major"

    @api.constrains("patient_age")
    def check_age(self):
        if self.patient_age <= 5:
            raise ValidationError(_("The age must be greater than 5"))

    def get_appointment_count(self):
        self.appointment_count = self.env['hospital.appointment'].search_count([('patient_id', '=', self.id)])

    def open_patient_appointments(self):
        return {
            'name': _("Appointment"),
            'domain': [('patient_id', '=', self.id)],
            'view_type': 'form',
            'res_model': 'hospital.appointment',
            'view_id': False,
            'view_mode': 'tree,form',
            'type': 'ir.actions.act_window',
        }
