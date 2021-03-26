from odoo import fields, models, api, _
from datetime import datetime
import pytz


class HospitalAppointment(models.Model):
    _name = 'hospital.appointment'
    _description = 'Appointment'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = "id desc"

    name = fields.Char(string="Appointment ID", required=True, copy=False, readonly=True,
                       index=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', string="Patient", required=True, default=1,  ondelete="cascade")
    patient_age = fields.Integer(string="Age", related='patient_id.patient_age')
    notes = fields.Text(string="Registration Note", default="Subscribe our youtube channel")
    doctor_note = fields.Text(string="Doctor note")
    pharmacy_note = fields.Text(string="Pharmacy note")
    appointment_date = fields.Date(string="Date", required=True, default=datetime.now())
    appointment_date_time = fields.Datetime(string="Date Time")
    active = fields.Boolean("Active", default=True)
    appointment_line = fields.One2many(comodel_name="hospital.appointment.lines", inverse_name="appointment_id",
                                       string="Appointment Lines")
    partner_id = fields.Many2one('res.partner', string="Customer")
    order_id = fields.Many2one('sale.order', string="Sale Order")

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

    def write(self, values):
        res = super(HospitalAppointment, self).write(values)
        return res

    def action_confirm(self):
        self.state = "confirm"

    def action_done(self):
        self.state = "done"

    def delete_lines(self):
        for rec in self:
            rec.appointment_line = [(5, 0, 0)]

    def print_time(self):
        for rec in self:
            print("time in utc", rec.appointment_date_time)
            user_tz = pytz.timezone(self.env.context.get('tz') or self.env.user.tz)
            print(user_tz)
            date_today = pytz.utc.localize(rec.appointment_date_time).astimezone(user_tz)
            print(date_today)

    @api.onchange('partner_id')
    def onchange_method(self):
        for rec in self:
            # rec.order_id = '' # initially empty
            return {'domain': {'order_id': [('partner_id', '=', rec.partner_id.id)]}}


class HospitalAppointmentLines(models.Model):
    _name = 'hospital.appointment.lines'
    _description = 'Appointment Lines'
    # _inherit = ['product.product']

    product_id = fields.Many2one("product.product", string="Medicine")
    product_qty = fields.Integer(string="Quantity")
    appointment_id = fields.Many2one(comodel_name="hospital.appointment", string='Appointment ID')
