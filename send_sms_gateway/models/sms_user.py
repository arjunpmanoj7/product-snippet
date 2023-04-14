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


class SmsUser(models.Model):
    """Saves the user credential details"""
    _name = 'sms.user'
    _description = "Sms User"
    _rec_name = 'gateway_name'

    api_method = fields.Char('API Method')
    url = fields.Char(sring='Gateway URL', help=' url for message')
    connection_ids = fields.One2many('sms.connection.params',
                                     'connection_gateway_id', 'Parameters')
    gateway_id = fields.Many2one('sms.gateway')
    gateway_name = fields.Char(related='gateway_id.name',
                               help='Gateway Name')
    vonage_key = fields.Char('key')
    vonage_secret = fields.Char()
    account_sid = fields.Char(string='Account Sid',
                              help="Account SID")
    auth_token = fields.Char(string='Auth Token', help="Auth token")
    customer_id = fields.Char(string="Customer ID", )
    d7_username = fields.Char(string="Username", help="D7 Username")
    d7_password = fields.Char(string="Password", help=" D7 Password")
    d7_from = fields.Char(string="From", help="D7 From Phone Number")
    api_key = fields.Char(string="API Key")
    telnyx_number = fields.Char(string="Telnyx Number", help="Telnyx "
                                                             "Number")
    telnyx_api_key = fields.Char(string="Api Key", help="Telnyx Api Key")
    messagebird_api_key = fields.Char(string="API Key", help="Message Api KeY")
    twilio_phone_number = fields.Char(string='Twilio Number',
                                      help="Twilio Phone Number")
