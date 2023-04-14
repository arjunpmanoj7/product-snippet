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
from odoo import fields, models


class FiscalYearPeriods(models.Model):
    _name = 'fiscal.periods'
    _rec_name = 'period_name'

    period_name = fields.Char(
        string='Period Name'
    )
    code = fields.Char(
        string='Code'
    )
    start_period = fields.Date(
        string='Starting Period'
    )
    end_period = fields.Date(
        string='End Date'
    )
    fiscal_year_id = fields.Many2one('fiscal.year')
    state = fields.Selection([('open', 'Open'),
                              ('close', 'Close')], default='open')


    def view_period(self):
        return {
            'name': '',
            'type': 'ir.actions.act_window',
            'res_model': 'fiscal.periods',
            'view_mode': 'form',
            'view_type': 'form',
            'target': 'current',
            'res_id': self.id

        }

    def close_period(self):
        self.state = 'close'

    def reopen(self):
        self.state = 'open'

    def cancel_periods(self):
        ids = self.env.context.get('active_ids')
        print(ids)
        for rec in ids:
            fiscal_periods = self.env['fiscal.periods'].browse(rec)
            for res in fiscal_periods:
                res.state = 'close'
