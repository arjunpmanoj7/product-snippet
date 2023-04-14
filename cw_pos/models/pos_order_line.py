from odoo import models, fields, api


class ProductTemplate(models.Model):
    _inherit = 'product.product'

    apply_cw = fields.Boolean()
    category_id = fields.Many2one('uom.category',
                                  default=lambda self: self.env.ref(
                                      'uom.product_uom_categ_kgm'))
    cw_uom_id = fields.Many2one('uom.uom', string='CW-Uom', stored=True,
                                help="Catch weight unit of measure",
                                domain="[('category_id', '=', category_id)]")
    catch_weigth_ok = fields.Boolean(default=False,
                                     string="Catch Weight Product")
    average_cw_qty = fields.Float(string='Catch Weight', digits=(16, 4),
                                  help="Catch weight quantity")
    catch_weight = fields.One2many('catch.weight', 'product_temp_con')

    @api.onchange('cw_uom_id', 'uom_id')
    def compute_weight(self):
        """Calculating cw qty if uom and cw uom category is same"""
        if self.uom_id.category_id == self.cw_uom_id.category_id:
            self.average_cw_qty = self.cw_uom_id.factor / self.uom_id.factor
        else:
            self.average_cw_qty = 1.00


class CatchWeight(models.Model):
    _name = 'catch.weight'

    value = fields.Float(digits=(10, 7))
    catch_weight_uom = fields.Many2one('uom.uom')
    product_temp_con = fields.Many2one('product.product')
    product_value = fields.Float()


class PosSession(models.Model):
    _inherit = 'pos.session'

    def _pos_ui_models_to_load(self):
        result = super()._pos_ui_models_to_load()
        result += [
            'catch.weight',
        ]
        print("fdfd", result)
        return result

    def _loader_params_catch_weight(self):
        return {
            'search_params': {
                # 'domain': [('id', '=', self.env['product.template'].search([('catch_weigth_ok','=','True')]).id)],
                'fields': [
                    'value', 'catch_weight_uom', 'product_temp_con','product_value'
                ],
            }
        }

    def _get_pos_ui_catch_weight(self, params):
        return self.env['catch.weight'].search_read(**params['search_params'])


