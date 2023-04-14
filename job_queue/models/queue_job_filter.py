from odoo import models, fields, api


class QueueJobFilter(models.Model):
    _name = 'queue.job.filter'

    model_fields_id = fields.Many2one(
        'ir.model.fields',
        string='Field'
    )
    selected_by = fields.Selection(
        [('is_set', 'is set'), ('is_not_set', 'is not set'), ('=', '='),
         ('>', '>'),
         ('!=', '!='), ('>', '>'), ('<', '<')])
    value = fields.Char(
        string='Field Value'
    )
    email_queue_jobs_id = fields.Many2one('email.queue.jobs')

    @api.onchange('model_fields_id')
    def onchange_report_id(self):
        return {'domain': {'model_fields_id': [
            ('model', '=', self.email_queue_jobs_id.report_id.model)]}}

