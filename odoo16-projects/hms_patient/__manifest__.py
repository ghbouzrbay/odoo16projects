{
    'name': 'Hospital Management System',
    'version': '1.0',
    'category': 'Healthcare',
    'summary': 'Manage hospital patient data',
    'author': 'Your Name',
    'website': 'https://www.example.com',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/hms_patient_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
