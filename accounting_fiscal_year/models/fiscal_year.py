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
from odoo import fields, models, api
from datetime import datetime
from dateutil import relativedelta
from dateutil.relativedelta import relativedelta
from odoo.exceptions import ValidationError
import calendar


class FiscalYear(models.Model):
    _name = 'fiscal.year'
    _inherit = "mail.thread", "mail.activity.mixin"
    _rec_name = 'fiscal_year_name'

    fiscal_year_name = fields.Char(
        string='Fiscal Year'
    )
    code = fields.Char(
        string='Code'
    )
    start_date = fields.Date(
        string='Start Date'
    )
    end_date = fields.Date(
        string='End Date'
    )
    fiscal_periods_ids = fields.One2many('fiscal.periods',
                                         'fiscal_year_id'
                                         )
    state = fields.Selection([('open', 'Open'),
                              ('close', 'Close'), ('draft', 'draft')],
                             default='draft')

    def compute_periods(self):
        self.write({'fiscal_periods_ids': [(5, 0, 0)]})
        first_date =self.start_date
        periods = self.write(
            {'fiscal_periods_ids': [(0, 0, {
                'period_name': "opening period" + str(self.start_date.year),
                'code': "00/" + str(self.start_date.year),
                'start_period': self.start_date,
                'end_period': self.start_date

            })]})
        delta = relativedelta(self.end_date, self.start_date)
        year = str(self.start_date.year)
        num = 1
        for i in range(1, delta.months + 2):
            res = calendar.monthrange(self.start_date.year,
                                      self.start_date.month)

            date = str(self.start_date.month) + '-' + str(res[1]) + '-' + str(
                self.start_date.year)

            date_object = datetime.strptime(date, '%m-%d-%Y').date()
            self.write({
                'fiscal_periods_ids': [(0, 0, {
                    'period_name': str(num) + '/' + year,
                    'code': str(num) + '/' + year,
                    'start_period': self.start_date,
                    'end_period': date_object,

                })]})
            num += 1
            self.start_date = self.start_date + relativedelta(months=1)
            self.state = 'open'
        self.write({'start_date':first_date})

    def cancel_fiscal_year(self):
        ids = self.env.context.get('active_ids')

        for rec in ids:
            year = self.env['fiscal.year'].browse(rec)
            for line in year:
                line.state = 'close'

            fiscal_periods = self.env['fiscal.periods'].search(
                [('fiscal_year_id', '=', rec)])
            for res in fiscal_periods:
                res.state = 'close'

    def reopen_fiscal(self):
        self.state = 'open'

    def cancel_fiscal(self):
        self.state = 'close'


class InheritAccountJournal(models.Model):
    _inherit = 'account.journal'

    type = fields.Selection(
        selection_add=[('opening_closing', 'Opening/Closing')],
        ondelete={'opening_closing': 'cascade'})
