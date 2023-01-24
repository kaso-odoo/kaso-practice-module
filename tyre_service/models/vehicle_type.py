# -*- coding: utf-8 -*-
from odoo import fields, models

class vehicle_type(models.Model):
    _name = "vehicle.type"
    _description = "vehicle type model"

    name=fields.Char(string="Name",required=True)