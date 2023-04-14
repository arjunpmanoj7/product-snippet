from odoo import fields, models


class DocumentFolders(models.Model):
    _name = 'document.folders'
    _description = 'Store Document Based on Folders'

    name = fields.Char('Folder Name', help="Name for the Folder")
    platform = fields.Selection(selection=[])
