from odoo import models, fields, api


class LearningAttendanceRegister(models.Model):
    _name = "learning.attendance.register"
    _inherit = ["mail.thread"]
    _description = "Attendance Register"

    name = fields.Char(
        'Name', size=16, required=True, track_visibility='onchange')
    code = fields.Char(
        'Code', size=16, required=True, track_visibility='onchange')
    course_id = fields.Many2one(
        'event.event', 'Course', required=True, track_visibility='onchange')
    batch_id = fields.Many2one(
        'learning.batch', 'Batch', required=True, track_visibility='onchange')
    subject_id = fields.Many2one(
        'learning.subject', 'Subject', track_visibility='onchange')

    _sql_constraints = [
        ('unique_attendance_register_code',
         'unique(code)', 'Code should be unique per attendance register!')]

    @api.onchange('course_id')
    def onchange_course(self):
        self.batch_id = False
