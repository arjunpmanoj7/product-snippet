from odoo import fields, models


class DocumentTags(models.Model):
    _name = 'document.tags'
    _description = 'Document Tags'

    name = fields.Char(string='Tag Category')
