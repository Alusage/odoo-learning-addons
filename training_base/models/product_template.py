# Copyright 2018 Nicolas JEUDY
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import api, fields, models, _


class ProductTemplate(models.Model):
    _inherit = ['product.template']

    is_training = fields.Boolean(string='is training')
    certificate = fields.Text(string='Certificate', translate=True)
    goal = fields.Text(string='Goal', translate=True)
    description = fields.Text(string='Description', translate=True)
    content = fields.Text(string='Content', translate=True)
    methodology = fields.Text(string='Methodology', translate=True)
    validate = fields.Text(string='Validate', translate=True)
    public = fields.Text(string='Public', translate=True)
    prerequisite = fields.Text(string='Prerequisite', translate=True)
    our_value = fields.Text(string='Value', translate=True)

    contact_id = fields.Many2one('res.partner', string="Contact")
    parent_domain_id = fields.Many2one('learning.domain',  related='domain_id.parent_id', store=True, string="Domain parent")
    domain_id = fields.Many2one('learning.domain', string="Domain")
    duration_info = fields.Char('Duration Info')
    price_info = fields.Char('Price info')
    duration_hour = fields.Float('Duration in hour(s)')
    cr_id = fields.Many2one('learning.cr', string="CR")
    training_code_id = fields.Many2one('learning.training.code')
    subject_ids = fields.One2many('learning.subject', 'product_id', string='Subject(s)')
    learning_level = fields.One2many('learning.level', 'learning_id', string="Level(s)")
    mediacla_id = fields.Many2one('learning.media_cla', string="MediaCLA")
    count_session = fields.Integer('Nb session', compute="_compute_session", readonly=True)
    nb_emprunt = fields.Integer('Nb Emprunt')
    nb_jour_autorise = fields.Integer('Nb jour autorisé')
    mediacla_code = fields.Char(related='mediacla_id.code', store=True, string="Mediacla Code")
    url_session = fields.Char("Url sessions", compute="_compute_url_session")
    idf = fields.Integer('IDF CLA')

    def _compute_url_session(self):
        for record in self:
            record.url_session = "http://www.formation-cla.univ-fcomte.fr/event?training_id=%s" % record.id

    def _compute_session(self):
        for record in self:
            record.count_session = len(self.env['event.event'].search([('training_id', '=', record.id)]))


class LearningCR(models.Model):
    _name = 'learning.cr'
    _parent_name = "parent_id"
    _parent_store = True

    name = fields.Char('Name')
    code = fields.Char('Code', translate=False)
    parent_id = fields.Many2one('learning.cr', 'Parent CR', index=True, ondelete='cascade')
    parent_path = fields.Char(index=True)
    child_id = fields.One2many('learning.cr', 'parent_id', 'Child CR')

    @api.constrains('parent_id')
    def _check_cr_recursion(self):
        if not self._check_recursion():
            raise ValidationError(_('You cannot create recursive CR.'))
        return True


class LearningTrainingCode(models.Model):
    _name = 'learning.training.code'

    name = fields.Char('Name')
    code = fields.Char('Code', translate=False)

class LearningMediacla(models.Model):
    _name = 'learning.media_cla'

    name = fields.Char('Name')
    code = fields.Char('Code', translate=False)
