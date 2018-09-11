from odoo import api, models, fields
from datetime import datetime
import requests
import bs4


class ClienteMic(models.Model):
    _inherit = 'res.partner'
    retencion = fields.Float('Retencion %')
    cabecera_ids = fields.One2many('mic.cabecera', 'partner_id')
