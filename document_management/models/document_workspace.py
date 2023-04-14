from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class DocumentWorkspace(models.Model):
    _name = 'document.workspace'
    _description = 'Document Workspace'

    name = fields.Char(string='Name', required=True,
                       help="Name of the WorkSpace.")
    display_name = fields.Char(string='Workspace',
                               compute='_compute_display_name',
                               help="Name of the WorkSpace.")
    parent_id = fields.Many2one('document.workspace',
                                string='Parent Workspace',
                                help="Current WorkSpace will be"
                                     " under this WorkSpace")
    company_id = fields.Many2one('res.company', string='Company',
                                 help="WorkSpace Belongs to this Company")
    description = fields.Text(string='Description',
                              help="Description about the WorkSpace")
    document_count = fields.Integer(compute='_compute_document_count',
                                    help="Number of Documents uploaded "
                                         "under this WorkSpace")
    folder_id = fields.Many2one('document.folders',
                                help="Folders of the WorkSpace")

    def btn_smart_document(self):
        return {
            'type': 'ir.actions.act_window',
            'res_model': 'document.file',
            'name': self.name,
            'view_mode': 'kanban,form',
            'view_type': 'form',
            'target': 'current',
            'domain': [('workspace_id', '=', self.id)]
        }

    def _compute_document_count(self):
        for record in self:
            record.document_count = self.env['document.file'].search_count(
                [('workspace_id', '=', self.id)])

    @api.constrains('parent_id')
    def _onchange_workspace_id(self):
        if self.parent_id == self.id:
            raise ValidationError("Cannot set current"
                                  " workspace as parent workspace !")
        else:
            return {
                'domain': {
                    'parent_id': [('id', '!=', self.id)]
                }
            }

    @api.model
    def work_spaces(self):
        workspaces = self.env['document.workspace'].search([])
        workspace_list = []
        for i in workspaces:
            workspace_list.append({
                'id': i.id,
                'name': i.name,
            })
        return workspace_list
