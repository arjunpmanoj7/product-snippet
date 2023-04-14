{
    'name': "POS Booking Order",
    'version': '16.0.1.0.0',
    'summary': """Book orders in pos""",
    'description': 'Book orders for customers in POS',
    'category': 'Point of Sale',
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    'depends': ['base', 'point_of_sale','pos_restaurant', 'pos_epson_printer_restaurant'],

    'data': [
        'data/data.xml',
        'security/ir.model.access.csv',
        # 'views/book_order.xml',
        'views/pos_config.xml',
    ],
    'demo': [],
    'images': [],
    'assets': {
        'point_of_sale.assets': [

            '/pos_kitchen_order/static/src/css/style.css',
            '/pos_kitchen_order/static/src/xml/kitchen_screen.xml',
            '/pos_kitchen_order/static/src/js/kitchen_screen.js',
            '/pos_kitchen_order/static/src/css/kitchen_screen.css',
            '/pos_kitchen_order/static/src/js/popup_1.js',
            '/pos_kitchen_order/static/src/js/kitchen_screen_order.js',
            '/pos_kitchen_order/static/src/xml/index.html',
        ]
    },
    'license': 'AGPL-3',
    'installable': True,
    'application': False,
}
