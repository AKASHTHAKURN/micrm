# -*- coding: utf-8 -*-
{
    'name' : 'MICrm BDO MI Backend Theme Version 10',
    'version' : '10.0.1.1.0',
    'author' : 'Suhendar',
    'category' : 'Backend Theme',
    'summary': 'cleaner bdo mi backend theme',
    'website' : 'http://www.bdo.co.id',
    'description': """
        Give BDO CRM cleaner theme, based on Bootstrap United template.
        The theme has also some css fixes for Microsoft Internet Explorer 11.
    """,
    'images':[
        #'images/sales.png'
    ],
    'depends' : ['base'],
    'data':[
        'views/webclient_templates.xml',
        ],
    'qweb': [
        'static/src/xml/base.xml',
        'static/src/xml/dashboard.xml',
        'views/database_manager.xml',
    ],
    'installable': True,
    'application' : False,
    'auto_install' : False
}
