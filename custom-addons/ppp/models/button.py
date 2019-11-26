from odoo import models,fields,api
def do_clear_done(self):
    is_child = self.search([('is_child', '=', False)])
    is_child.write(True)
    return True