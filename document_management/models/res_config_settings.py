from odoo import models, fields, api


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    cloud_sync = fields.Boolean('Cloud Sync', default=False,
                                help="Enable this field to Sync with Cloud")
    trash = fields.Integer('Trash Limit', default=30,
                           help="set the time limit for the deleted files",
                           config_parameter='document_management.trash')

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        res['cloud_sync'] = self.env['ir.config_parameter'].sudo().get_param(
            "base.cloud_sync", default="")
        return res

    @api.model
    def set_values(self):
        self.env['ir.config_parameter'].set_param("base.cloud_sync",
                                                  self.cloud_sync or '')
        super(ResConfigSettings, self).set_values()


