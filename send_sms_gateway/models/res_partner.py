# -*- coding: utf-8 -*-
################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Cybrosys Techno Solutions (Contact : odoo@cybrosys.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0
#    (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the
#    Software or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
#    OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE
#    USE OR OTHER DEALINGS IN THE SOFTWARE.
#
################################################################################
from odoo import models, _


class ResPartner(models.Model):
    """Inheriting model res_partner to write the function to send sms"""
    _inherit = 'res.partner'

    def send_sms_gateway(self):
        """Function to add send sms as server action"""
        record = self.env.context.get('active_ids')
        numbers = self.env['res.partner'].browse(record).mapped('phone')
        return {

            'name': _('Send Sms'),
            'type': 'ir.actions.act_window',
            'res_model': 'send.sms',
            'context': {
                'default_sms_to': ','.join([str(numb) for numb in numbers]),
            },
            'view_mode': 'form',
            'target': 'new'
        }
