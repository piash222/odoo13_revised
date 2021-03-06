{
    'name': 'Hospital Management',
    'version': '13.0.1.0.0',
    'summary': 'Module for managing the hospitals',
    'sequence': '10',
    'category': 'Extra tools',
    'author': 'Shihab Uddin',
    'website': 'shihabuddin.me',
    'license': 'AGPL-3',
    'depends': [
        'mail', 'product', 'odoo_report_xlsx', 'sale', 'website'
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/sequence.xml',
        'data/data.xml',
        'data/cron.xml',
        'data/mail_template.xml',
        'views/patient.xml',
        'views/appointment.xml',
        'views/doctor.xml',
        'views/lab.xml',
        'wizards/create_appointment.xml',
        'reports/patient_card.xml',
        'reports/report.xml',
        'reports/sale_report_inherit.xml',
        'views/template.xml',
        'reports/appointment.xml'
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
