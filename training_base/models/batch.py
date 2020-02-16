from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class LearningBatch(models.Model):
    _name = 'learning.batch'

    code = fields.Char('Code', size=16, required=True)
    name = fields.Char('Name', size=32, required=True)
    start_date = fields.Date(
        'Start Date', required=False, default=fields.Date.today())
    end_date = fields.Date('End Date', default=fields.Date.today(),  required=False)
    course_id = fields.Many2one('event.event', 'Course', required=True)

    _sql_constraints = [
        ('unique_batch_code',
         'unique(code)', 'Code should be unique per batch!')]

    @api.multi
    @api.constrains('start_date', 'end_date')
    def check_dates(self):
        for record in self:
            start_date = fields.Date.from_string(record.start_date)
            end_date = fields.Date.from_string(record.end_date)
            if start_date > end_date:
                raise ValidationError(_("End Date cannot be set before \
                Start Date."))

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('get_parent_batch', False):
            lst = []
            lst.append(self.env.context.get('course_id'))
            courses = self.env['event.event'].browse(lst)
            batches = self.env['learning.batch'].search([('course_id', 'in', lst)])
            return batches.name_get()
        return super(LearningBatch, self).name_search(
            name, args, operator=operator, limit=limit)
