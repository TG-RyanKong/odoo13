# -*- coding: utf-8 -*-
{
    'name': 'student',
    'description': 'Extend the PPP app to multiuser.',
    'summary': """
        this is a student's system""",
    'author': 'Ryan Kong',
    'depends':['ppp'],
    'website': "http://www.mypscloud.com",
    'application': True,
    'category': 'Uncategorized',
    'version': '1.0',
    # any module necessary for this one to work correctly
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
 }
