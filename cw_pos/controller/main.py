from odoo import http, _
from odoo.http import request


class PosRequest(http.Controller):
    @http.route('/pos_request_route', type='json', auth='user')
    def pos_func(self, **kw):
        option = False
        if kw['option']:
            option = int(kw['option'])
        catch_weight = request.env['catch.weight'].search([

            ('catch_weight_uom', '=', option),
            ('product_temp_con', '=', kw['product_id'])
        ])
        print('kw', kw['product_id'], kw['option'])
        print('kw', kw['unit'])
        uom = request.env['uom.uom'].browse([(kw['unit'])])
        uom_ratio = uom.ratio
        unit = kw['unit']
        quantity = kw['quantity']
        value = catch_weight.value
        cal = value * uom_ratio * quantity
        print("calculation",cal)

        vals = {'message': 2,
                'calculation':cal}

        return vals
