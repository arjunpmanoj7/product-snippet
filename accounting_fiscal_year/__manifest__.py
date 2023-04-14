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
    'name': 'Accounting Fiscal Year',
    'version': '16.0.1.0.0',
    'summary': """Accounting Fiscal Year""",
    'description': """Accounting Fiscal Year""",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://cybrosys.com/",
    'depends': ['base', 'account', 'mail'],
    'data': ['security/ir.model.access.csv',
             'views/fiscal_year_view.xml',
             'views/fiscal_periods_view.xml',
             'views/fiscal_periods_action.xml',
             'views/fiscal_year_action.xml',
             'data/account_journal.xml',
             'views/inherit_account_move_view.xml',
             'views/group_by_fiscal.xml',
             'views/inherit_res_config_view.xml',
             'wizard/opening_entry_view.xml',
             'wizard/cancel_closing_entry_view.xml',
             ],
    'license': 'AGPL-3',
    'installable': True,
    'auto_install': False,
    'application': False,
}
