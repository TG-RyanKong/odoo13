# -*- coding: utf-8 -*-
from odoo import http

class Ppp(http.Controller):
    @http.route('/ppp/ppp/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/ppp/ppp/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('ppp.listing', {
            'root': '/ppp/ppp',
            'objects': http.request.env['ppp.ppp'].search([]),
        })

    @http.route('/ppp/ppp/objects/<model("ppp.ppp"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('ppp.object', {
            'object': obj
        })