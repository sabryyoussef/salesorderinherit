from odoo import models, fields

class ConstructionProject(models.Model):
    _name = 'construction.project'
    _description = 'Construction Project'

    name = fields.Char(string='Project Name', required=True)
    start_date = fields.Date(string='Start Date')
    end_date = fields.Date(string='End Date')
    budget = fields.Float(string='Budget')
    company_id = fields.Many2one('res.partner', string='Construction Company', required=True)
    location = fields.Char(string='Location')
    project_manager_name = fields.Char(string='Project Manager Name')
    project_manager_email = fields.Char(string='Project Manager Email')
    project_manager_mobile = fields.Char(string='Project Manager Mobile')
    message_ids = fields.One2many('mail.message', 'res_id', string='Messages',
                                  domain=lambda self: [('model', '=', self._name)], auto_join=True)
    message_follower_ids = fields.One2many('mail.followers', 'res_id', string='Followers',
                                           domain=lambda self: [('res_model', '=', self._name)], auto_join=True)
    activity_ids = fields.One2many('mail.activity', 'res_id', string='Activities',
                                   domain=lambda self: [('res_model', '=', self._name)], auto_join=True)


