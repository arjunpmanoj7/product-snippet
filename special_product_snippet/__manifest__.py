# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2022-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Arjun P Manoj(odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
################################################################################
{
    'name': 'special product website snippet',
    'version': '16.0.1.0.0',
    'summary': """special product website snippet""",
    'category': 'Tools',
    'description': """special product website snippet""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://cybrosys.com/",
    'depends': ['sale_management', 'website', 'base', 'stock', 'website_sale'],
    'data': ['views/product_snippet_template.xml',
             'views/product_snippets_option.xml',
             ],
    'assets': {
        'web.assets_frontend': [
            'special_product_snippet/static/src/css/product_snippet.css',
        ],
        'website.assets_wysiwyg': [
            '/special_product_snippet/static/src/js/options.js'
        ],

        'web.assets_backend': [
            'special_product_snippet/static/src/xml/template.xml',
        ],

    },
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
