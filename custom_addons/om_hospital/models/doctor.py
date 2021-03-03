from odoo import fields, models, api


class HospitalDoctor(models.Model):
    _name = 'hospital.doctor'
    _description = 'Doctor Record'

    name = fields.Char(string='Name', required=True)
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'),
                   ('fe_male', 'Female'), ], default='male',
        required=False)
    user_id = fields.Many2one('res.users', string='Related User', required=True)
