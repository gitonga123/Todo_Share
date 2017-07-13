# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoTask(models.Model):
	_inherit = ['todo.task']
	user_id = fields.Many2one('res.users','Responsible')
	date_deadline = fields.Date('Deadline')
	name = fields.Char(help="What needs to be done?")
	stage_id = fields.Many2one('todo.task.stage','Stage')
	tag_ids = fields.Many2many('todo.task.tag',string='Tags')

	@api.multi
	def do_clear_done(self):
		domain = [('is_done','=', True),
					'|',('user_id','=',self.env.uid),
					 ('user_id','=',False)]
		dones = self.search(domain)
		dones.write({'active': False})
		return True


	@api.multi
	def do_toggle_done(self):
		for task in self:
			if task.user_id != self.env.user:
				raise ValidationError('Only the responsible can do this!')
		return super(TodoTask, self).do_toggle_done()


class Tag(models.Model):
	_name = 'todo.task.tag'
	_description= 'To-do Tag'
	name = fields.Char('Name',size=40,translate=True)
	task_ids = fields.Many2many('todo.task',"Tags")
	



class stage(models.Model):
	_name='todo.task.stage'
	_description = 'To-do Stage'
	_order = 'sequence,name'

	name = fields.Char('Name',size=40, translate=True)
	sequence = fields.Integer('Sequence')
	desc = fields.Text('Description')
	state = fields.Selection([('draft','New'),('open','Started'),
		('done','Closed')],'State')
	docs = fields.Html('Documentation')
	perc_complete = fields.Float('% Complete',(3,2))

	date_effective = fields.Date('Effective Date')
	date_changed = fields.Datetime('Last Changed')
	fold = fields.Boolean('Folded?')
	image = fields.Binary('Image')
	task_ids = fields.One2many('todo.task','stage_id',string="Tasks in this Stage")