{
    'name': 'Js Class Blog',
    'version': '16.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Cybrosys Techno solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base', 'web', 'sale'],
    'data': ['views/inherit_sale_order.xml'],
    'assets': {
        'web.assets_backend': [
            'js_class_blog/static/src/js/formrender.js',
            'js_class_blog/static/src/js/formview.js',

        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3'
}
