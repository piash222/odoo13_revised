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
        'mail',
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'patient.xml',
    ],
    'demo': [

    ],
    'installable': True,
    'application': True,
    'auto_install': False
}
