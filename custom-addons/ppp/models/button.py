from odoo import models,fields

class p2Task(models.Model):
    _name = 'p1.child'
    _description = 'have child'
    def is_child_done(self):
            Task = self.env['p1.child']
            done_stage = Task.search([('is_child', '=', 'Ture')])
            for checkout in self:
                checkout.is_child = done_stage
            return True