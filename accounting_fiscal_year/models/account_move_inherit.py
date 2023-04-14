from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
class InheritAccountMove(models.Model):
    _inherit = 'account.move'

    periods_id = fields.Many2one('fiscal.periods', readonly=True, store=True)
    fiscal_year_id = fields.Many2one('fiscal.year', readonly=True, store=True)
    journal_entry = fields.Boolean()

    @api.onchange('invoice_date')
    def _onchange_period(self):
        params = self.env['ir.config_parameter'].sudo()
        fiscal_year = params.get_param(
            'account_fiscal_year.fiscal_year_id')
        period = self.env['fiscal.periods'].search(
            [('start_period', '<=', self.invoice_date),
             ('end_period', '>=', self.invoice_date),
             ('fiscal_year_id', '=', int(fiscal_year))])

        self.periods_id = period.id
        self.fiscal_year_id = self.periods_id.fiscal_year_id.id

    def action_post(self):

        params = self.env['ir.config_parameter'].sudo()
        restrict_period = params.get_param(
            'account_fiscal_year.restrict_period')

        if restrict_period:
            if self.periods_id.state == 'close':
                raise ValidationError('This period is closed')
            if self.fiscal_year_id.state == 'close':
                raise ValidationError('This fiscal year is closed')

        return super(InheritAccountMove, self).action_post()
