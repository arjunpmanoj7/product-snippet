import base64
from odoo import models, fields, api
import logging
from itertools import accumulate
from datetime import datetime, timedelta
from odoo.exceptions import ValidationError

_logger = logging.getLogger(__name__)


class MyModel(models.Model):
    _name = 'email.jobs'
    _rec_name = 'email'

    name = fields.Char(
        string='Name'
    )
    email = fields.Char(
        string='Email'
    )


class ScheduledDate(models.Model):
    _name = 'scheduled.date'

    name = fields.Char()


class MyOtherModel(models.Model):
    _name = 'email.queue.jobs'
    _inherit = "mail.thread", "mail.activity.mixin"

    recipients_email_ids = fields.Many2many(
        'email.jobs', required=True
    )
    name = fields.Char(
        string='Name', required=True
    )

    models_id = fields.Many2one(
        'ir.model'
    )
    report_id = fields.Many2one(
        'ir.actions.report', required=True

    )
    queue_job_filter_ids = fields.One2many('queue.job.filter',
                                           'email_queue_jobs_id')

    schedule_by = fields.Selection(
        [('daily', 'Daily'), ('weekly', 'Weekly')])

    state = fields.Selection(
        [('draft', 'Draft'), ('running', 'Running'), ('canceled', 'Canceled')],
        default='draft')

    week = fields.Selection([('0', 'Monday'), ('1', 'Tuesday'),
                             ('2', 'Wednesday'),
                             ('3', 'Thursday'),
                             ('4', 'Friday'),
                             ('5', 'Saturday'),
                             ('6', 'Sunday')], default='0')

    start_date = fields.Date(readonly=True)
    eta = fields.Integer()
    next_excution_date = fields.Datetime(readonly=True)

    def button_cancel(self):
        self.write({'state': 'canceled'})

    def button_reopen(self):
        self.write({'state': 'running'})

    @api.onchange('queue_job_filter_ids')
    def onchange_filter(self):
        for line in self.queue_job_filter_ids:
            if line.models_fields_id.ttype not in ['many2one', 'char',
                                                   'integer', 'float']:
                raise ValidationError('Sorry cannot adapt the value')

    def next_date(self, day):
        day_num = int(day)
        add_days = timedelta(days=1)
        next_day = datetime.now() + add_days
        while next_day.weekday() != day_num:
            next_day += add_days
        return next_day.strftime('%b %d %Y')

    @api.onchange('schedule_by')
    def onchange_schedule_by_daily(self):
        if self.schedule_by == 'daily':
            tomorrow = self.start_date + timedelta(1)
            self.eta = int((tomorrow - self.start_date).total_seconds())
            self.next_excution_date = datetime.now() + timedelta(days=1)

    @api.onchange('week')
    def onchange_schedule_by(self):
        self.start_date = fields.Datetime.now()
        if self.schedule_by == 'weekly':
            day = self.week
            next_date = self.next_date(day)
            datetime_object = datetime.strptime(next_date,
                                                '%b %d %Y')
            self.next_excution_date = datetime_object
            self.eta = int((
                                   self.next_excution_date - fields.Datetime.now()).total_seconds())

    def button_start(self):
        self.write({'state': 'running'})

    def action_schedule_jobs(self):
        jobs = self.env['email.queue.jobs'].search([('state', '=', 'running')])
        for job in jobs:
            if job.schedule_by == 'weekly':
                if job.next_excution_date == fields.Datetime.now():
                    job.next_excution_date = datetime.now() + timedelta(days=7)
                    job.eta = 604800

            self.with_delay(eta=job.eta).delayed_mailing(job)

    def delayed_mailing(self, job):
        fields_name = []
        length_to_split = []
        domain_list = []
        if job.schedule_by == 'daily':
            daily_record = (datetime.now() - timedelta(days=2)).date()
            daily_record_between = (datetime.now()).date()
            date_by = ['create_date', '<', daily_record_between]
            date_between = ['create_date', '>', daily_record]
            domain_list.append(tuple(date_by))
            domain_list.append(tuple(date_between))
        if job.schedule_by == 'weekly':
            weekly_record = (datetime.now() - timedelta(days=6)).date()
            weekly_record_2 = (datetime.now()).date()
            date_by = ['create_date', '>=', weekly_record]
            date_from = ['create_date', '<=', weekly_record_2]
            domain_list.append(tuple(date_by))
            domain_list.append(tuple(date_from))

        for val in job.queue_job_filter_ids:
            fields_name.append(val.model_fields_id.name)
            fields_name.append(val.selected_by)

            if val.model_fields_id.ttype in ['many2one', 'integer']:
                fields_name.append(int(val.value))
            elif val.model_fields_id.ttype == 'float':
                fields_name.append(float(val.value))

            else:
                fields_name.append(val.value)
            length_to_split.append(3)
        Output = [fields_name[x - y: x] for x, y in zip(
            accumulate(length_to_split), length_to_split)]
        for line in Output:
            domain_tuple = tuple(line)
            domain_list.append(domain_tuple)
        account_list = []
        account_record = self.env[job.report_id.model].search(
            domain_list)
        if account_record:
            for rec in account_record:
                account_list.append(rec.id)
            generated_report = job.report_id._render_qweb_pdf(
                job.report_id.report_name, res_ids=account_list)

            data_record = base64.b64encode(generated_report[0])

            ir_values = {'name': job.name,
                         'type': 'binary',
                         'datas': data_record,
                         'store_fname': data_record,
                         'mimetype': 'application/pdf',
                         'res_model': job.report_id.model,
                         }

            report_attachment = self.env['ir.attachment'].sudo().create(
                ir_values)

            email_template = self.env['mail.template'].create({
                'name': 'Reports',
                'subject': 'Email Reports',
                'body_html': '<p>Hey Please Check Your Report</p>',
                'auto_delete': True,
                'model_id': self.env.ref(
                    'job_queue.model_email_queue_jobs').id
            })
            email_values = {
                'email_to': job.recipients_email_ids.email,
                'email_from': job.env.user.email,
            }
            email_template.attachment_ids = [(4, report_attachment.id)]

            email_template.send_mail(
                job.id, email_values=email_values,
                force_send=True)
            email_template.attachment_ids = [(5, 0, 0)]
