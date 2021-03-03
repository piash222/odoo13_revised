from odoo import fields, models, api, _
from datetime import datetime

class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    name = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True, default=1)
    patient_age = fields.Integer(string="Age", related='patient_id.patient_age')
    notes = fields.Text(string="Registration Note", default="Subscribe our youtube channel")
    doctor_note = fields.Text(string="Doctor note")
    pharmacy_note = fields.Text(string="Pharmacy note")
    appointment_date = fields.Date(string="Date", required=True, default=datetime.now())
    state = fields.Selection(
        selection=[('draft', 'Draft'),
                   ('confirm', 'Confirm'),
                   ('done', 'Done'),
                   ('cancel', 'Canceled')],
        string='Status', readonly=True, default='draft')

    @api.model
    def create(self, vals_list):
        if vals_list.get('name', _('New')) == _('New'):
            vals_list['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
            result = super(HospitalAppointment, self).create(vals_list)
            return result

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"
