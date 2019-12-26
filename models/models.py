from odoo import models, fields, api, _

class stageinvoices(models.Model):
    _inherit = 'account.invoice'
    _name = 'account.invoice'
    
    stages = fields.Many2one(
        string='Stages',
        comodel_name='vit_stage_invoice.stage'
    )
    


    

    

    
