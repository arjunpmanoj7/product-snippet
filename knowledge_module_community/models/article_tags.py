from odoo import models, fields


class ArticleTags(models.Model):
    _name = 'article.tags'

    name = fields.Char(string='Tags')


