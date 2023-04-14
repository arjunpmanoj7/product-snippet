from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal
from odoo import fields
import base64


class WebsiteCustomerPortal(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        values = super(WebsiteCustomerPortal,self)._prepare_home_portal_values(counters)
        if 'document_count' in counters:
            user_id = request.uid
            document_count = request.env['document.file'].sudo().search_count([
                ('user_id.id', '=', user_id)
            ])
            request_count = request.env['request.document'].sudo().search_count([
                ('user_id.id', '=', user_id),
                ('state', '=', 'requested')
            ])
            values['document_count'] = document_count
            values['request_count'] = request_count
        return values


class DocumentPortalView(http.Controller):

    @http.route('/my/documents', type="http", auth="public", website=True)
    def document_in_portal(self):
        user_id = request.uid
        extension = []
        document_ids = request.env['document.file'].sudo().search([
            ('user_id.id', '=', user_id)
        ])
        for item in document_ids:
            if item.extension not in extension:
                extension.append(item.extension)
        context = []
        for item in extension:
            items = []
            for rec in document_ids:
                if rec.extension == item:
                    items.append(rec)
            context.append(items)
        values = {
            'extensions': extension,
            'document_ids': context,
            'page_name': 'document',
        }
        return request.render("document_management.portal_my_documents", values)

    @http.route('/my/document_request', type="http", auth="public",
                website=True)
    def document_request_in_portal(self):
        user_id = request.uid
        request_ids = request.env['request.document'].sudo().search([
            ('user_id.id', '=', user_id),
            ('state', '=', 'requested')
        ])
        context = []
        for item in request_ids:
            context.append({
                'id': item.id,
                'needed_doc': item.needed_doc,
                'workspace_id': [item.workspace_id.id, item.workspace_id.name],
                'requested_by': [item.requested_by.id, item.requested_by.name],
                'user_id': [item.user_id.id, item.user_id.name],
                'date': item.create_date.date()
            })
        values = {
            'requests': context,
            'page_name': 'document_requests',
        }
        return request.render("document_management.portal_my_document_request",
                              values)

    @http.route('/my/documents/<model("document.file"):doc>', type="http",
                auth="public", website=True)
    def document_view(self, doc):
        owner = doc.user_id
        activity_ids = []
        for activity in doc.activity_ids:
            activity_ids.append({
                'activity_name': activity.activity_type_id.name,
                'activity_summary': activity.summary,
                'activity_date_deadline': activity.date_deadline,
            })
        context = {
            'page_name': 'document',
            'document': True,
            'name': doc.name,
            'id': doc.id,
            'owner': owner,
            'attachment_id': doc.attachment_id.id,
            'brochure_url': doc.brochure_url,
            'workspace_id': doc.workspace_id.name,
            'date': doc.date,
            'url': f"{request.httprequest.host_url[:-1]}/web/content/{doc.attachment_id.id}/{doc.name}",
            'access_token': doc.attachment_id.access_token,
            'partner_id': doc.partner_id.name,
            'extension': doc.extension,
            'preview': doc.preview,
            'content_url': doc.content_url,
            'activity_ids': activity_ids,
        }
        return request.render("document_management.portal_my_document_view",
                              context)


class WebsiteDocumentsUpload(http.Controller):

    @http.route('/website/documents', type="http", auth="public",
                website=True, csrf=False)
    def website_docs(self, **post):
        pri = post['file'].stream
        filename = post['file'].filename
        workspace = post['workspace']
        description = post['reason']
        security = post['security']
        if security == 'Private':
            file_id = request.env['document.file'].create({
                'name': filename,
                'attachment': base64.b64encode(pri.read()),
                'workspace_id': int(workspace),
                'date': fields.Date.today(),
                'user_id': request.env.uid,
                'description': description,
                'security': 'private',
                'extension': filename.split(".")[
                    len(filename.split(".")) - 1]
            })
            file_id.upload_document()

        else:
            file_id = request.env['document.file'].create({
                'name': filename,
                'attachment': base64.b64encode(pri.read()),
                'workspace_id': int(workspace),
                'date': fields.Date.today(),
                'user_id': request.env.uid,
                'description': description,
                'security': 'managers_and_owner',
                'extension': filename.split(".")[
                    len(filename.split(".")) - 1]
            })
            file_id.upload_document()

        return request.redirect("/my/documents")

    @http.route('/website/documents_request', type="http", auth="public",
                website=True, csrf=False)
    def website_docs_request(self, **post):
        rec_id = post['rec_id']
        request_id = request.env['request.document'].browse(int(rec_id))
        pri = post['file'].stream
        filename = post['file'].filename
        workspace = post['workspace']
        description = post['reason']
        requested_by = post['requested_by']
        file_id = request.env['document.file'].sudo().create({
            'name': filename,
            'attachment': base64.b64encode(pri.read()),
            'workspace_id': int(workspace),
            'date': fields.Date.today(),
            'user_id': request.env.uid,
            'description': description,
            'security': 'specific_users',
            'user_ids': [requested_by],
            'extension': filename.split(".")[
                len(filename.split(".")) - 1]
        })
        file_id.upload_document()
        request_id.state = 'accepted'
        return request.redirect("/my/document_request")

    @http.route('/website/documents_request_reject', type="http", auth="public",
                website=True, csrf=False)
    def document_request_reject(self, **post):
        rec_id = post['req_id']
        request_id = request.env['request.document'].browse(int(rec_id))
        description = post['reason']
        request_id.state = 'rejected'
        request_id.reject_reason = description

        return request.redirect("/my/document_request")
