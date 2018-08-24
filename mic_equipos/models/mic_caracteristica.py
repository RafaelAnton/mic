# -*- coding: utf-8 -*-
from odoo import models, fields, api


class Caracteristica_Equipo(models.Model):
    _name = "mic.caracteristica"
    _rec_name = 'caracteristica_nombre'
    caracteristica_nombre = fields.Char(String='Nombre de Datos Asociados')
