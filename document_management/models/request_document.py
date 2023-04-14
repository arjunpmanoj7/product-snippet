from odoo import fields, models, api, _


class RequestDocumentUser(models.Model):
    _name = 'request.document'
    _description = 'Request document from user'
    _rec_name = 'needed_doc'

    user_id = fields.Many2one('res.users', string='User')
    requested_by = fields.Many2one('res.users',
                                   default=lambda self:self.env.user)
    needed_doc = fields.Text(string='Document Needed', required=True)
    workspace_id = fields.Many2one('document.workspace', string='Work space')
    reject_reason = fields.Text(string='Reason')
    state = fields.Selection(selection=[
        ('requested', 'Requested'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')], default='requested')

    @api.model
    def action_request_doc(self, workspace_id):
        return {
            'type': 'ir.actions.act_window',
            'name': _('Add Document Request'),
            'res_model': 'request.document',
            'view_mode': 'form',
            'target': 'new',
            'views': [[False, "form"]],
            'context': {
                'default_workspace_id': workspace_id
            }
        }

    def send_document_request(self):
        doc_id = self.user_id.id
        return {
            'type': 'ir.actions.act_window',
            'name': 'mail',
            'res_model': 'mail.compose.message',
            'view_mode': 'form',
            'target': 'new',
            'views': [[False, 'form']],
            'context': {
                'default_partner_ids': [doc_id],
                'default_body': f'Dear ' + ' ' + self.user_id.name
                                + '<p>please attach the '
                                  'requested document - </p>'
                                + self.needed_doc
                                + '<p>Regards</p>' + 'Manager' + '</p>'
                + self.requested_by.name,
            }
        }

    @api.model
    def get_request(self):
        context = []
        request_ids = self.env['request.document'].search(
            [('user_id', '=', self.env.uid)])
        for rec in request_ids:
            context.append({
                'request_id': rec.id,
                'user_id': rec.user_id.name,
                'manager_id': rec.manager_id.name,
                'needed_doc': rec.needed_doc,
                'workspace': rec.workspace.name,
                'workspace_id': rec.workspace.id,
            })
        return context

