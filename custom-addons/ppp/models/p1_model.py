# –*– coding: utf–8 –*–
from odoo import models,fields

class p1Task(models.Model):
    _name = 'p1.task'
    _description = 'P1 Task'
    name = fields.Char('name', required=True)
    age = fields.Char('age')
    marry = fields.Boolean('marry')
    is_child = fields.Boolean('child', default = False)

