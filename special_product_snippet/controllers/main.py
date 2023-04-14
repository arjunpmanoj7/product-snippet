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
from odoo import http, _
from odoo.http import request
import json


class SpecialProduct(http.Controller):

    """ getting product details  and passing returnig
        the values and rendering the templates from js"""

    @http.route('/website/snippet/special/render', type='json', auth='public',
                website=True)
    def render_template(self, template, params):
        res = json.loads(params)
        product = request.env['product.template'].sudo().search_read(
            [('id', '=', res['id'])])
        qcontext = {}
        for rec in product:
            qcontext['display_name'] = rec['display_name']
            qcontext['list_price'] = rec['list_price']
            qcontext['website_url'] = rec['website_url']
            qcontext[
                'image_url'] = '/web/image/product.template/%s/image_1920' % \
                               rec['id']
        return {
            'qcontext': qcontext
        }


