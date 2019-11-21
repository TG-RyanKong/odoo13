# –*– coding: utf–8 –*–
from odoo import models, fields

class p1Task(models.Model):
    _name = 'p1.task'
    _description = 'P1 Task'
    name = fields.Char('Description', required=True)
    age = fields.Char('age')
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)