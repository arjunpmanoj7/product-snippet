
{
    'name': "Catch Weight - POS",
    'description': """
        Allows to enable Catch Weight Management System in 
    POS Module
    """,
    'summary': """Catch Weight Management In POS Module""",
    'version': '16.0.1.0.0',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': 'https://www.cybrosys.com',
    'category': 'POS',
    'depends': ['base','point_of_sale','stock'],
    'data': ['security/ir.model.access.csv',
        'views/order_line.xml',
    ],
    'assets': {
        'point_of_sale.assets': [
            'cw_pos/static/src/js/cw8_button.js',
            'cw_pos/static/src/js/load_fields.js',
            'cw_pos/static/src/js/cw8_popup.js',
            'cw_pos/static/src/views/cw8_button.xml',
            'cw_pos/static/src/views/cw8_template.xml',
            'cw_pos/static/src/views/receipt_template_views.xml'
        ],
    },
    # 'images': ['static/description/banner.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
    'auto_install': False,

}
