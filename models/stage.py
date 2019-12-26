
from odoo import api, fields, models
import time
import datetime
import logging
_logger = logging.getLogger(__name__)


class stages(models.Model):
    _name = 'vit_stage_invoice.stage'
    _description = 'New Description'

    name = fields.Char(
        string='Name',
        required=True,
    )
    
    usage = fields.Selection(
        string='Usage',
        selection=[('in invoice', 'in invoice'), 
                   ('out invoice', 'out invoice')],
    )
    
