from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'
    project_id = fields.Many2one('construction.project', string='Construction Project')

    state = fields.Selection([
        ('draft', 'Qutation'),
        ('engineering_review', 'Engineering'),
        ('manager_review', 'Management'),
        ('approved', 'Approved'),
        ('refused', 'Rejected'),
        ('refused', 'Qutation Sent'),
        ('sale', 'Sales Order'),
    ], default='draft')

    def action_submit_to_engineering(self):
        self.ensure_one()
        # Perform any necessary checks before transitioning to the engineering review stage
        self.state = 'engineering_review'

    def action_approve_engineering(self):
        self.ensure_one()
        # Logic to handle approval by engineering
        self.state = 'manager_review'

    def action_refuse_engineering(self):
        self.ensure_one()
        # Logic to handle refusal by engineering
        self.state = 'refused'

    def action_submit_to_manager(self):
        self.ensure_one()
        # Logic to handle submission to manager
        self.state = 'manager_review'

    def action_reset_to_draft(self):
        self.ensure_one()
        # Logic to reset quotation back to draft
        self.state = 'draft'

# how to open form view in button click
# link https://www.youtube.com/watch?v=lwhAHQMV0DU&t=50s
# def my_button(self):
#     return {
#         'name': "Your String",
#         'type': 'ir.actions.act_window',
#         'view_type': 'form',
#         'view_mode': 'form',
#         'res_model': 'object',
#         'view_id': self.env.ref('module.view_id').id,
#         'target': 'new'
#     }