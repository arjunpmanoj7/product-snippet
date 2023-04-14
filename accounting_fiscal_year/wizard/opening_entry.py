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
from odoo import models, fields, api


class OpenEntry(models.TransientModel):
    _name = 'opening.entries'

    fiscal_year_close = fields.Many2one('fiscal.year',
                                        srting='Fiscal Year To Close',
                                        required=True
                                        )
    Opening_journal_entry = fields.Many2one(
        'account.journal',
        required=True
    )

    new_fiscal_year = fields.Many2one(
        'fiscal.year',
        string='New Fiscal Year',
        required=True
    )
    opening_entries_period = fields.Many2one(
        'fiscal.periods',
        string='Opening Entries Period',
        domain="[('fiscal_year_id','=',new_fiscal_year)]",
        required=True
    )

    def create_entry(self):
        closing_journal = self.env['account.move'].search(
            [('fiscal_year_id', '=', self.fiscal_year_close.id)])
        debit = 0
        credit = 0
        for rec in closing_journal.line_ids:
            debit += rec.debit
            credit += rec.credit

        credit_account = self.env['account.account'].search(
            [('code', '=', 757575)])
        debit_account = self.env['account.account'].search(
            [('code', '=', 757576)])

        account_move = self.env['account.move'].create({
            'ref': 'opening balance entry',
            'periods_id': self.opening_entries_period.id,
            'fiscal_year_id': self.new_fiscal_year.id,
            'journal_id': self.Opening_journal_entry.id,
            'line_ids': [
                (0, 0, {
                    'account_id': credit_account.id,
                    'credit': credit,
                    'name': 'credit centralization'
                }),
                (0, 0, {
                    'account_id': debit_account.id,
                    'debit': debit,
                    'name': 'debit centralization'

                }),
            ],

        })
        account_move.journal_entry = True
