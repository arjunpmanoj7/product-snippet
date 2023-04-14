from odoo import fields, models, api, _
from odoo.http import request
import base64
from zipfile import ZipFile
from datetime import timedelta


class Document(models.Model):
    _name = 'document.file'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Documents for Community'

    name = fields.Char(string="Name")
    attachment = fields.Binary(string='File')
    date = fields.Datetime(string='Date')
    workspace_id = fields.Many2one('document.workspace', string='Workspace',
                                   required=True)
    user_id = fields.Many2one('res.users', string='Owner',
                              default=lambda self: self.env.user,
                              check_company=True,
                              index=True, tracking=True)
    brochure_url = fields.Char("URL", store=True)
    extension = fields.Char(string='Extension')
    priority = fields.Selection([
        ('0', 'None'),
        ('1', 'Favorite'),
    ], string="Priority")
    activity_ids = fields.One2many(
        'mail.activity', string='Activities')
    boolean = fields.Boolean('Boolean', default=False)
    attachment_id = fields.Many2one('ir.attachment')
    content_url = fields.Char('Content Url')
    content_type = fields.Selection(
        selection=[
            ('file', 'File'),
            ('url', 'Url')
        ]
    )
    preview = fields.Char('Preview')
    active = fields.Boolean(string='Active', default=True)
    deleted_date = fields.Date()
    mimetype = fields.Char(string='Mime Type')
    description = fields.Text(string='Description')
    security = fields.Selection(
        selection=[
            ('private', 'Private'),
            ('managers_and_owner', 'Managers & Owner'),
            ('specific_users', 'Specific Users')
        ], default='managers_and_owner'
    )
    user_ids = fields.Many2many('res.users')
    partner_id = fields.Many2one('res.partner')
    task = fields.Boolean(default=False, compute='_compute_task')
    lead = fields.Boolean(default=False, compute='_compute_lead')
    auto_delete = fields.Boolean(string='Auto Delete', default=False)
    days = fields.Integer(string='Days')
    trash = fields.Boolean(string='Trash')
    delete_date = fields.Date(string='Date Delete', readonly=True, store=True)
    file_url = fields.Char(string='File URL')

    @api.model
    def _compute_task(self):
        project = self.env['ir.module.module'].search(
            [('name', '=', 'project')])
        for rec in self:
            if project.state == 'installed':
                rec.task = True
            else:
                rec.task = False

    @api.model
    def _compute_lead(self):
        crm = self.env['ir.module.module'].search([('name', '=', 'crm')])
        for rec in self:
            if crm.state == 'installed':
                rec.lead = True
            else:
                rec.lead = False

    @api.onchange('days')
    def _onchange_days(self):
        date = fields.Date.today()+timedelta(days=self.days)
        self.write({
            'delete_date': date,
        })

    def auto_delete_doc(self):
        document = self.env['document.file'].search([
            ('auto_delete', '=', True)
        ])
        for doc in document:
            if doc.delete_date:
                if fields.Date.today() <= doc.delete_date:
                    doc.unlink()

    def edit_documents(self):
        return {
            'name': self.name,
            'type': 'ir.actions.act_window',
            'target': 'current',
            'view_mode': 'form',
            'res_model': 'document.file',
            'res_id': self.id,
        }

    def upload_document(self):
        self.sudo().write({
            'name': self.name,
            'date': fields.Date.today(),
            'user_id': self.env.uid,
            'extension': self.name.split(".")[len(self.name.split(".")) - 1]
        })
        attachment_id = self.env['ir.attachment'].sudo().create(
            {'name': self.name,
             'datas': self.attachment,
             'res_model': 'document.file',
             'res_id': self.id,
             }
        )
        self.content_url = f"{request.httprequest.host_url[:-1]}/web/content/{attachment_id.id}/{self.name}"
        self.mimetype = attachment_id.mimetype
        self.attachment_id = attachment_id.id
        self.brochure_url = attachment_id.local_url
        url = str(request.httprequest.host_url[:-1]) + self.brochure_url
        oo = (base64.b64encode(attachment_id.name.encode("ascii"))).decode(
            "ascii")
        url2 = str(request.httprequest.host_url[:-1]) + "/document/%s/%s" % (
            attachment_id.id, oo)
        self.brochure_url = url
        return {
            'type': 'ir.actions.client',
            'tag': 'reload'
        }

    @api.model
    def document_file_create(self, value, name, workspace):
        x = name.split(".")
        workspace_id = self.env['document.workspace'].search(
            [('id', '=', workspace)])
        try:
            data = value.split('base64')[1] if value else False
        except TypeError:
            data = value
        document = self.create({
            'name': name,
            'attachment': data,
            'date': fields.Date.today(),
            'workspace_id': workspace_id.id,
            'user_id': self.env.uid,
            'extension': name.split(".")[len(name.split(".")) - 1]
        })
        attachment_id = self.env['ir.attachment'].create(
            {'name': document.name,
             'datas': data,
             'res_model': 'document.file',
             'res_id': self.id,
             }
        )
        document.attachment_id = attachment_id.id
        document.brochure_url = attachment_id.local_url
        url = str(request.httprequest.host_url[:-1]) + document.brochure_url
        oo = (base64.b64encode(attachment_id.name.encode("ascii"))).decode(
            "ascii")
        url2 = str(request.httprequest.host_url[:-1]) + "/document/%s/%s" % (
            attachment_id.id, oo)
        document.brochure_url = url
        return 1

    @api.model
    def document_information(self, record_id):
        file_data = self.env["document.file"].search([('id', '=', record_id)])
        file_owner = self.env["res.users"].browse(file_data.user_id.id)
        file_workspace = self.env["document.workspace"].browse(
            file_data.workspace_id.id)
        file_info = {
            'filename': file_data.name,
            'filetype': file_data.extension,
            'owner': file_owner.name,
            'workspace': file_workspace.name,
            'file_size': file_data.attachment_id.file_size,
            'mimetype': file_data.attachment_id.mimetype
            }
        return file_info

    @api.model
    def archive_function(self, document_selected):
        document_path = self.env['document.file'].search(
            [('id', 'in', document_selected)])
        length = len(document_path)
        zip_obj = ZipFile('attachments.zip', 'w')
        for i in range(length):
            zip_obj.write(document_path[i].attachment_id._full_path(
                document_path[i].attachment_id.store_fname),
                         document_path[i].attachment_id.name)
        zip_obj.close()
        return {
            'type': 'ir.actions.act_url',
            'url': f"{request.httprequest.host_url[:-1]}/web/attachments/download",
            'target': 'self',
        }

    @api.model
    def download_local(self, document_selected):
        doc_id = self.env['document.file'].browse(document_selected)
        return {
            'type': 'ir.actions.act_url',
            'url': f"/web/content/{doc_id.attachment_id.id}?download=true&amp;access_token=",
            'target': 'self',
        }

    @api.model
    def document_file_delete(self, ids):
        document_ids = self.env['document.file'].browse(ids)
        for rec in document_ids:
            rec.trash = True
            rec.delete_date = fields.Date.today()
            rec.active = False

    @api.model
    def document_file_archive(self, documents_selected):
        documents_active = self.search([('id', 'in', documents_selected)])
        documents_un = self.search(
            [('id', 'in', documents_selected), ('active', '=', False)])
        for docs in documents_active:
            docs.active = False
        for docs in documents_un:
            if docs.delete_date:
                docs.delete_date = False
            docs.active = True

    @api.model
    def document_file_preview(self, record_ids):
        rec_id = self.env['document.file'].browse(record_ids)
        return {
            'type': 'ir.actions.act_url',
            'target': 'self',
            'url': rec_id.brochure_url,
        }

    @api.model
    def on_mail_document(self, doc_ids):
        attachment_ids = self.env['document.file'].browse(doc_ids).mapped(
            'attachment_id')
        return {
            'type': 'ir.actions.act_window',
            'name': 'mail',
            'res_model': 'mail.compose.message',
            'view_mode': 'form',
            'target': 'new',
            'views': [[False, 'form']],
            'context': {
                'default_attachment_ids': attachment_ids.ids,
            }
        }

    @api.model
    def on_copy_document(self, doc_id):
        return {
            'type': 'ir.actions.act_window',
            'name': 'copy',
            'res_model': 'work.space',
            'view_mode': 'form',
            'target': 'new',
            'views': [[False, 'form']],
            'context': {
                'default_doc_id': doc_id['doc_id']
            }
        }

    @api.model
    def action_add_url(self, workspace_id):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Add Url'),
            'res_model': 'document.url',
            'view_mode': 'form',
            'target': 'new',
            'views': [[False, "form"]],
            'context': {
                'default_workspace_id': workspace_id,
            }
        }

    @api.model
    def action_btn_create_task(self, doc):
        document = self.search([('id', 'in', doc)])
        if len(document) != 0:
            for rec in document:
                name = rec['name'].split('.')
                task_id = self.env['project.task'].create({
                    'name': name[0]
                })
                rec.attachment_id.res_model = 'project.task'
                rec.attachment_id.res_id = task_id
            return True
        else:
            return False

    @api.model
    def action_btn_create_lead(self, doc):
        document = self.search([('id', 'in', doc)])
        if len(document) != 0:
            for rec in document:
                name = rec['name'].split('.')
                lead_id = self.env['crm.lead'].create({
                    'name': name[0]
                })
                rec.attachment_id.res_model = 'crm.lead'
                rec.attachment_id.res_id = lead_id
            return True
        else:
            return False

    @api.model
    def delete_doc(self):
        document = self.env['document.file'].search([('active', '=', False),
                                                     ('trash', '=', True)])
        limit = self.env['ir.config_parameter'].sudo().get_param(
            'document_management.trash')
        for doc in document:
            if doc.deleted_date:
                delta = fields.Date.today() - doc.deleted_date
                if delta.days == limit:
                    doc.unlink()
