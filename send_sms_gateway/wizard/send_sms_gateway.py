# -*- coding: utf-8 -*-
######################################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2023-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author:  Cybrosys Techno Solutions (odoo@cybrosys.com)
#
#    This program is under the terms of the Odoo Proprietary License v1.0 (OPL-1)
#    It is forbidden to publish, distribute, sublicense, or sell copies of the Software
#    or modified copies of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
#    DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
#    ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#    DEALINGS IN THE SOFTWARE.
#
########################################################################################
from odoo import fields, models, _
from odoo.exceptions import UserError

import requests

import messagebird
from telesign.messaging import MessagingClient
import telnyx
import vonage

from twilio.rest import Client


class WizardSms(models.TransientModel):
    """Fields to add the sms gateway and send to number"""

    _name = 'send.sms'
    _description = "SmS send wizard"

    sms_id = fields.Many2one(string='sms.user')
    sms_to = fields.Char(string="Send TO", help="Number to send sms")
    text = fields.Text(string="Text", required=True,
                       help="Enter the text for the sms")

    def sms_send(self):
        """
        Function to send sms using different sms gateway using the api
        response of different gateway
        """

        if self.sms_id.gateway_name == 'vonage':
            client = vonage.Client(key=self.sms_id.vonage_key,
                                   secret=self.sms_id.vonage_secret)
            vonage.Sms(client)
            numbers = self.sms_to.split(',')
            for numb in numbers:
                if numb:
                    client.sms.send_message(
                        {
                            "from": 'Vonage APIs',
                            "to": numb,
                            "text": self.text,
                        }
                    )
        elif self.sms_id.gateway_name == "twilio":
            account_sid = self.sms_id.account_sid
            auth_token = self.sms_id.auth_token
            client = Client(account_sid, auth_token)
            numbers = self.sms_to.split(',')
            for numb in numbers:
                if numb:
                    client.messages.create(
                        body=self.text,
                        from_=self.sms_id.twilio_phone_number,
                        to=numb
                    )
        elif self.sms_id.gateway_name == "telesign":
            customer_id = self.sms_id.customer_id
            api_key = self.sms_id.api_key
            numbers = self.sms_to.split(',')
            for numb in numbers:
                if numb:
                    phone_number = numb
                    message = self.text
                    message_type = "ARN"
                    messaging = MessagingClient(customer_id, api_key)
                    messaging.message(phone_number, message,
                                      message_type)
        elif self.sms_id.gateway_name == "d7":
            url = "https://http-api.d7networks.com/send"
            numbers = self.sms_to.split(',')
            for numb in numbers:
                if numb:
                    querystring = {
                        "username": self.sms_id.d7_username,
                        "password": self.sms_id.d7_password,
                        "from": self.sms_id.d7_from,
                        "content": """This%20is%20a%20test%20message%20to%20
                        verify%20the%20DLR%20callback""",
                        "dlr-method": "POST",
                        "dlr-url": "https://4ba60af1.ngrok.io/receive",
                        "dlr": "yes",
                        "dlr-level": "3",
                        "to": numb
                    }
                    headers = {
                        'cache-control': "no-cache"
                    }
                    requests.request("GET", url, headers=headers,
                                     params=querystring)
        elif self.sms_id.gateway_name == "messagebird":
            client = messagebird.Client('P5s0yhVRc4HaLEMNnBzC8b7XY')
            numbers = self.sms_to.split(',')
            for numb in numbers:
                if numb:
                    try:
                        client.message_create(
                            'MessageBird',
                            numb,
                            self.text,
                            {'reference': 'Foobar'}
                        )
                    except messagebird.client.ErrorException:
                        raise UserError('Invalid parameter')
        elif self.sms_id.gateway_name == "telnyx":
            telnyx.api_key = self.sms_id.telnyx_api_key
            numbers = self.sms_to.split(',')
            for numb in numbers:
                if numb:
                    your_telnyx_number = self.sms_id.telnyx_number
                    destination_number = numb
                    try:
                        telnyx.Message.create(
                            from_=your_telnyx_number,
                            to=destination_number,
                            text=self.text,
                        )
                    except telnyx.error.InvalidRequestError:
                        raise UserError('Missing required parameter')
        self.env['sms.history'].sudo().create({
            'gateway_name': self.sms_id.gateway_id.id,
            'sms_mobile': self.sms_to,
            'sms_text': self.text,

        })
