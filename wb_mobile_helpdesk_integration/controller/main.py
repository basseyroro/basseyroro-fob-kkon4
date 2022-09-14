import json
from odoo import http, _
from odoo.http import request


class SupportMobileAPI(http.Controller):

    @http.route('/get/customer/list', type='json', auth='api_key')
    def getCustomerList(self, **kwargs):
        request_data = json.loads(request.httprequest.data)
        page = request_data.get("page", 1)
        return request.env['wb.mobile.request.registration'].getCustomerList(page)

    @http.route('/get/company/list', type='json', auth='api_key')
    def getCompanyList(self, **kwargs):
        request_data = json.loads(request.httprequest.data)
        page = request_data.get("page", 1)
        return request.env['wb.mobile.request.registration'].getCompanyList(page)

    @http.route('/get/helpdesk/team/list', type='json', auth='api_key')
    def getHelpdeskTeamList(self, **kwargs):
        request_data = json.loads(request.httprequest.data)
        page = request_data.get("page", 1)
        return request.env['wb.mobile.request.registration'].getHelpdeskTeamList(page)

    @http.route('/get/helpdesk/list', type='json', auth='api_key')
    def getHelpdeskList(self, **kwargs):
        request_data = json.loads(request.httprequest.data)
        page = request_data.get("page", 1)
        return request.env['wb.mobile.request.registration'].getHelpdeskList(page)

    @http.route('/get/team/list', type='json', auth='api_key')
    def getTeamList(self, **kwargs):
        request_data = json.loads(request.httprequest.data)
        page = request_data.get("page", 1)
        return request.env['wb.mobile.request.registration'].getTeamList(page)

    @http.route('/assign/team/member', type='json', auth='api_key', methods=["POST"])
    def assignTeamMember(self, **kwargs):
        request_data = json.loads(request.httprequest.data)
        fse_id = request_data.get("fse_id", 0)
        ticket_id = request_data.get("ticket_id", 0)
        return request.env['wb.mobile.request.registration'].getHelpdeskList(vals={'fse_id':fse_id, 'ticket_id':ticket_id})