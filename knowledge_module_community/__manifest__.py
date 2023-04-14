{
    'name': 'Knowledge Module Community v16',
    'version': '16.0.1.0.0',
    'summary': '',
    'description': '',
    'category': 'Extra Tools',
    'author': 'Cybrosys Techno solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base', 'web','mail'],
    'data': ['security/ir.model.access.csv',
             'views/myknowledgearticle.xml',
             'views/html_views_option.xml',
             'views/myknowledge_views.xml',
             'views/article_tags.xml'],
    'assets': {
        'web.assets_backend': [
            'knowledge_module_community/static/src/js/myknowledgeformrender.js',
            # 'knowledge_module_community/static/src/js/formcontroller.js',
            'knowledge_module_community/static/src/js/formview.js',
            'knowledge_module_community/static/src/css/myarticle.css',
            # 'knowledge_module_community/static/src/xml/section_template.xml'

        ],
        'web_editor.assets_wysiwyg': [
            'knowledge_module_community/static/src/js/htmloption.js'
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3'
}
