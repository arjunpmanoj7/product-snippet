from odoo import fields, models


class POSUserKitchen(models.Model):
    _inherit = 'res.user'

    kitchen_screen_user = fields.Selection([
        ('manager', 'Manager'), ('waiter', 'Waiter'), ('cook', 'Cook')
    ], string='Kitchen screen user')
    can_delete_order_line = fields.Boolean(string='Can delete Orderline')
    reason_delete_order_line = fields.Boolean(string='Reason for delete Orderline')
    pos_category = fields.Many2many('pos.category', string='Pos categories')
