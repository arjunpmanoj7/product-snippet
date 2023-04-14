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
from odoo import fields, models


class SmsHistory(models.Model):
    """Model to store the history of sent SMS messages"""
    _name = 'sms.history'
    _description = "History"
    _rec_name = 'sms_mobile'

    gateway_name_id = fields.Many2one('sms.gateway', string="Gateway Name",
                                      help="Gateway Name")
    sms_date = fields.Datetime(string="Date", default=fields.Date().today())
    sms_mobile = fields.Char(string="Mobile Ph",
                             help="Phone Number to send sms")
    sms_text = fields.Text(string="Sms Text")

    sms_history_company_id = fields.Many2one('res.company',
                                             required=True,
                                             default=lambda
                                                 self: self.env.company)
