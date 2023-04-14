from odoo import models, fields, api, _
from odoo.http import request
import uuid


class DocumentShare(models.Model):
    _name = 'document.share'
    _description = 'Document Share'

    url = fields.Char('Document Url', readonly=True)
    document_ids = fields.Many2many('document.file')
    user_ids = fields.Many2many('res.users')
    unique_id = fields.Char('Unique Access ID', readonly=True)

    @api.model
    def create_url(self, document_ids):
        unique_id = uuid.uuid4()
        url = f"{request.httprequest.host_url[:-1]}/web/content/share/?unique={unique_id}"
        self.create({
            'url': url,
            'document_ids': document_ids,
            'unique_id': unique_id
        })
        return {
            'type': 'ir.actions.act_window',
            'name': _('Share'),
            'res_model': 'document.share',
            'view_mode': 'form',
            'target': 'new',
            'views': [[False, "form"]],
            'context': {
                'default_url': url
            }
        }
