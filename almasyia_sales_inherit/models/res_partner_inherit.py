from odoo import models, fields, api
class ResPartner(models.Model):
    _inherit = 'res.partner'

    project_ids = fields.One2many('construction.project', 'company_id', string='Projects')
