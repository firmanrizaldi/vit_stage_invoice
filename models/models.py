from odoo import models, fields, api, _

class stageinvoices(models.Model):
    _inherit = 'account.invoice'
    _name = 'account.invoice'


    # stages = fields.Selection(
    #     string='Stages',
    #     selection=[('AR 1', 'AR 1'), 
    #     ('AR 2', 'AR 2'),
    #     ('AR 3', 'AR 3'),])
    
    stages = fields.Many2one(
        string='Stages',
        comodel_name='vit_stage_invoice.stage'
    )
    


    

    

    
