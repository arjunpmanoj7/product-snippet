{
    'name': 'pos pre ordering',
    'version': '16.0.1.0.0',
    'summary': 'pos pre ordering',
    'description': 'This module helps to make pre ordering option in pos',
    'category': 'Extra Tools',
    'author': 'Cybrosys Techno solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'depends': ['base', 'web', 'point_of_sale'],
    'assets': {
        'point_of_sale.assets': [
            'pos_pre_ordering/static/src/xml/pre_order_popup.xml',
            'pos_pre_ordering/static/src/js/pre_order.js',
            'pos_pre_ordering/static/src/xml/pre_order.xml',
            'pos_pre_ordering/static/src/js/pre_order_popup.js'

        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'AGPL-3'
}
