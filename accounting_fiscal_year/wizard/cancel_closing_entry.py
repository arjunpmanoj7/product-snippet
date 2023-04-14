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
from odoo import models, fields


class CancelClosingEntry(models.Model):
    _name = 'cancel.closing.entry'

    fiscal_year_id = fields.Many2one(
        'fiscal.year', required=True
    )

    def cancel_journal_entry(self):
        cancel_entry = self.env['account.move'].search(
            [('fiscal_year_id', '=', self.fiscal_year_id.id),
             ('journal_entry', '=', True)])
        cancel_entry.unlink()
