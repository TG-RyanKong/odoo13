# –*– coding: utf–8 –*–
from odoo import models, fields,exceptions
import logging

class p1Task(models.Model):
    _name = 'p1.task'
    _description = 'P1 Task'
    name = fields.Char('name', required=True)
    age = fields.Char('age')
    marry = fields.Boolean('marry')
    is_child = fields.Boolean('child', default=False)

    def is_child_done(self):
       # Stage = self.env['p1.task']
        # for Stage in self:
        self.is_child = True

    def no_child_done(self):

        self.age = 23
        self.is_child = False

