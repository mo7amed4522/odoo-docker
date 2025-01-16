{
    'name': 'Hospital Management',
    'version': '1.0',
    'summary': 'Hospital Management System',
    'sequence': 10,
    'author': 'Odoo Community Association (OCA)',
    'description': """
    Hospital Management System
    """,
    'category': 'Extra Tools',
    'website': 'https://www.odoo.com/page/hospital-management-system',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/base_model.xml',
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}