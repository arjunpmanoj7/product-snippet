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
{
    'name': " Send SMS",
    'version': '16.0.1.0.0',
    'description': "This modules helps to send sms using different gateway",
    'summary': "Module sends sms through different sms gateway",
    'author': "Cybrosys Techno Solutions",
    'category': "Extra Tools",
    'website':"https://www.cybrosys.com",
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'depends': ['base', 'contacts'
                ],
    'data': [
        'security/send_sms_gateway_group.xml',
        'security/sms_history_security.xml',
        'security/ir.model.access.csv',
        'data/sms_gateway_list_data.xml',
        'views/sms_history_views.xml',
        'views/sms_user_views.xml',
        'views/action_send_sms_gateway.xml',
        'wizard/wizard_sms_views.xml',
        'views/sms_menu_views.xml'
    ],
    # "external_dependencies": {
    #     "python": ["messagebird", "telnyx", "twilio", "vonage", "telesign"]},

    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
}
