{
    'name': 'thong tin',
    'version': '1.0',
    'author': 'Your Name',
    'category': 'Human Resources',
    'summary': 'Quản lý thông tin cá nhân nhân viên',
    'depends': ['base', 'hr'],
    'data': [
        'views/employee_views.xml',
        'views/ir_model_access.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}

