# �C*�C coding: utf�C8 �C*�C
from odoo.tests.common import TransactionCase

class TestTodo(TransactionCase):
	def test_create(self): "Create a simple Todo"
	Todo = self.env['todo.task']
	task = Todo.create(('name': 'Test Task'}) 
	self.assertEqual(task.is_done, False)