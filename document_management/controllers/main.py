from odoo import http
from odoo.http import request


class DocumentFile(http.Controller):
    @http.route('/web/content/share/', type='http', auth='public',
                website='True')
    def document_share(self, **kwargs):
        folder_ids = request.env['document.share'].sudo().search([
            ('unique_id', '=', kwargs.get('unique'))
        ])
        context = []
        for document in folder_ids.document_ids :
            context.append({
                'doc_id': document.id,
                'doc_name': document.name,
                'doc_extension': document.extension,
                'doc_owner': document.user_id,
                'doc_date': document.date,
                'doc_url': document.content_url,
            })
        values = {
            'context': context
        }

        return http.request.render('document_management.document_share_preview',
                                   values)


class DownloadController(http.Controller):
    @http.route("/web/attachments/download", type="http")
    def download_zip(self):
        return http.send_file(
            filepath_or_fp='./attachments.zip',
            mimetype="application/zip",
            as_attachment=True,
            filename="attachments.zip",
        )


class DownloadLocal(http.Controller):
    @http.route("/web/attachments/download_local", type="http")
    def download_zip(self):
        print("controller")
        return http.send_file(
            filepath_or_fp='./attachments.zip',
            mimetype="application/zip",
            as_attachment=True,
            filename="attachments.zip",
        )
