# -*- coding: utf-8 -*-

from odoo import models, fields, api

class ppp(models.Model):
    _name = 'ppp.ppp'

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    value3 = fields.Char()
    value4 = fields.Char()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100