from odoo import models, fields, api


@api.model
def _lang_get(self):
    return self.env['res.lang'].get_installed()


class WizardStudentRegistration(models.TransientModel):
    _name = 'wizard.student_from_event_registration'
    _description = "Create Student from event registration"

    def _default_category(self):
        return self.env['res.partner.category'].browse(self._context.get('category_id'))

    def _default_company(self):
        return self.env['res.company']._company_default_get('res.partner')

    already_student = fields.Boolean("Link to existing student ?", default=False)
    student_id = fields.Many2one("learning.student", "Existing Student")
    birth_date = fields.Date('Birth Date')
    gender = fields.Selection(
        [('male', 'Male'), ('female', 'Female')], 'Gender')
    nationality = fields.Many2one('res.country', 'Nationality')
    visa_info = fields.Char('Visa Info', size=64)
    id_number = fields.Char('ID Card Number', size=64)
    already_partner = fields.Boolean('Already Partner')
    partner_id = fields.Many2one(
        'res.partner', 'Partner')
    is_student = fields.Boolean(default=True)
    title = fields.Many2one('res.partner.title')
    image = fields.Binary("Image", attachment=True,
        help="This field holds the image used as avatar for this contact, limited to 1024x1024px",)
    lang = fields.Selection(_lang_get, string='Language', default=lambda self: self.env.lang,
                            help="If the selected language is loaded in the system, all documents related to "
                                 "this contact will be printed in this language. If not, it will be English.")
    category_id = fields.Many2many('res.partner.category',
                                   column1='partner_id',
                                   column2='category_id', string='Tags', default=_default_category)
    type = fields.Selection(
        [('contact', 'Contact'),
         ('invoice', 'Invoice address'),
         ('delivery', 'Shipping address'),
         ('other', 'Other address'),
         ("private", "Private Address"),
        ], string='Address Type',
        default='contact',
        help="Used to select automatically the right address according to the context in sales and purchases documents.")
    street = fields.Char()
    street2 = fields.Char()
    zip = fields.Char(change_default=True)
    city = fields.Char()
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict')
    country_id = fields.Many2one('res.country', string='Country', ondelete='restrict')
    email = fields.Char()
    phone = fields.Char()
    mobile = fields.Char()
    name = fields.Char(
        "Name",
        index=True,
    )
    event_registration_id = fields.Many2one("event.registration", string="Event registration")

    @api.model
    def default_get(self, fields):
        res = super(WizardStudentRegistration, self).default_get(fields)
        if not res.get('event_registration_id'):
            event_registration_id = res.get('event_registration_id', self._context.get('active_id'))
            res['event_registration_id'] = event_registration_id
        event_registration = self.env['event.registration'].browse(res.get('event_registration_id'))
        res['email'] = event_registration.email
        res['phone'] = event_registration.phone
        res['name'] = event_registration.name
        res = self._convert_to_write(res)
        return res

    @api.multi
    def action_create_student(self):
        active_id = self.env.context.get('active_ids', []) or []
        event_registration = self.env['event.registration'].browse(active_id)

        for record in self:
            if not record.already_student:
                vals = {
                    'name': record.name,
                    'country_id': record.nationality.id,
                    'gender': record.gender,
                    'phone': record.phone,
                    'phone': record.email,
                    'birth_date': record.birth_date,
                }
                if record.already_partner:
                    vals["partner_id"] = partner_id.id
                student_id = self.env['learning.student'].create(vals)
            else:
                student_id = record.student_id
            event_registration.write({'student_id': student_id.id})
        return {'type': 'ir.actions.act_window_close'}
