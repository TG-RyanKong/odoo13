# –*– coding: utf–8 –*–

from odoo import models, fields,api
from odoo.exceptions import ValidationError

# class TodoTask(models.Model):
#     _inherit = 'p1.task'
#     user_id = fields.Many2one('res.users', 'Responsible')
#     date_deadline = fields.Date('Deadline')


@api.multi
def is_child_done(self):
    for task in self:
        if task.user_id == self.env.user:
           raise ValidationError('Only the responsible can do this!')
           return super(TodoTask,self).is_child_done()