from odoo import models, fields, api


class WizardOpFacultyEmployee(models.TransientModel):
    _name = 'wizard.learning.teacher.employee'
    _description = "Create Employee and User of Teacher"

    user_boolean = fields.Boolean("Want to create user too ?", default=True)

    @api.multi
    def create_employee(self):
        for record in self:
            active_id = self.env.context.get('active_ids', []) or []
            teacher = self.env['learning.teacher'].browse(active_id)
            teacher.create_employee()
            if record.user_boolean and not teacher.user_id:
                user_group = self.env.ref('training_base.group_learning_teacher')
                self.env['res.users'].create_user(teacher, user_group)
