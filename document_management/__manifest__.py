{
    'name': 'Document Management',
    'version': '16.0.1.0.0',
    'summary': 'Document management',
    'category': '',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'mail', 'website', 'portal'],
    'website': 'https://cybrosys.com',
    'data': [
        'data/workspace.xml',
        'data/trash.xml',
        'security/document_management_security.xml',
        'security/ir.model.access.csv',
        'views/document_workspace.xml',
        'views/document_file.xml',
        'views/res_configuration.xml',
        'views/menu.xml',
        'views/document_portal.xml',
        'views/request_document_view.xml',
        'views/portal_my_document_view.xml',
        'views/document_request_portal.xml',
        'wizards/document_share.xml',
        'wizards/document_url.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'https://unpkg.com/sweetalert/dist/sweetalert.min.js',
            'document_management/static/src/css/kanban.css',
            '/document_management/static/src/xml/ListController.xml',
            '/document_management/static/src/xml/KanbanController.xml',
            '/document_management/static/src/js/search_panel_extention_model.js',
            '/document_management/static/src/js/kanbancontroller.js',
            '/document_management/static/src/js/listcontroler.js',
            '/document_management/static/src/js/search_document.js',
            '/document_management/static/src/js/side_panel.js',
            'https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.6/dist/jquery.fancybox.min.css',
            'https://cdn.jsdelivr.net/npm/@fancyapps/fancybox@3.5.6/dist/jquery.fancybox.min.js'

        ],
        'web.assets_frontend': [
            '/document_management/static/src/js/my_portal.js',
        ]
    },
    'images': ['/static/description/banner.png'],
    'license': 'OPL-1',
    'currency': 'EUR',
    'installable': True,
    'auto_install': False,
    'application': False,
}
# -*- coding: utf-8 -*-
