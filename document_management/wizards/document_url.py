from odoo import models, fields, api
from linkpreview import Link, LinkPreview, LinkGrabber


class WorkSpace(models.TransientModel):
    _name = 'work.space'
    workspace_id = fields.Many2many('document.workspace',
                                    string='Workspace', required=True)
    doc_id = fields.Many2many('document.file')
    move = fields.Boolean(compute="_compute_move", default=True)

    @api.onchange('workspace_id')
    def _compute_move(self):
        if len(self.workspace_id)>1:
            self.move = False
        else:
            self.move = True

    def copy_docs(self):
        for workspace in self.workspace_id.ids:
            for rec in self.doc_id:
                self.env['document.file'].create({
                    'name': rec.name,
                    'attachment': rec.attachment,
                    'attachment_id': rec.attachment_id.id,
                    'date': fields.Date.today(),
                    'workspace_id': workspace,
                    'user_id': rec.user_id.id,
                    'extension': rec.name.split(".")[len(rec.name.split(".")) - 1]
                })
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }

    def move_docs(self):
        for rec in self.doc_id:
            rec.write({
                'workspace_id': self.workspace_id
            })
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }


class UrlUploadWizard(models.TransientModel):
    _name = 'document.url'
    _description = 'Url Upload Wizard'

    url = fields.Char('Url')
    workspace_id = fields.Many2one('document.workspace', required=True)
    name = fields.Char('Name')
    preview = fields.Char('Url Preview')

    @api.onchange('url')
    def action_fetch_url(self):
        self.preview = None
        if self.url:
            url = self.url
            grabber = LinkGrabber(
                initial_timeout=20, maxsize=1048576, receive_timeout=10,
                chunk_size=1024,
            )
            content, url = grabber.get_content(url)
            link = Link(url, content)
            preview = LinkPreview(link, parser="lxml")
            self.name = preview.title
            self.preview = preview.image

    def action_add_url(self):
        self.env['document.file'].create({
            'name': self.name,
            'date': fields.Date.today(),
            'workspace_id': self.workspace_id.id,
            'user_id': self.env.uid,
            'extension': 'url',
            'content_url': self.url,
            'content_type': 'url',
            'preview': self.preview,
            'brochure_url': self.url
        })
        return {
            'type': 'ir.actions.client',
            'tag': 'reload',
        }
