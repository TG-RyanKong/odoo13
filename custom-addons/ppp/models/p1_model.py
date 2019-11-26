# –*– coding: utf–8 –*–
from odoo import models, fields,api

class p1Task(models.Model):
    _name = 'p1.task'
    _description = 'P1 Task'
    name = fields.Char('name', required=True)
    age = fields.Char('age')
    marry = fields.Boolean('marry')
    is_child = fields.Boolean('child', default = False)

@api.multi
def do_toggle_done(self):
    for task in self:
        task.is_child = not task.is_child
    return True