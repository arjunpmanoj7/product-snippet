from odoo import fields, models
from odoo.tools.safe_eval import json
from odoo.addons.web.controllers.utils import clean_action


class MyKnowledgeArticle(models.Model):
    _name = 'my.knowledge.article'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'My Knowledge Article'

    name = fields.Char(string='Title', required=True)
    author_id = fields.Many2one('res.partner', string='Author')
    article_body = fields.Html()
    tags = fields.Many2many('article.tags', string='Tags')
    feedback = fields.Boolean()

    def chatter_knowledge(self):

        if self.feedback:
            self.feedback = False
            return False
        else:
            self.feedback = True
            return True
