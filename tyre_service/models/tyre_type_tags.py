# -*- coding: utf-8 -*-
from odoo import fields, models

class tyre_service_tag(models.Model):
    _name = "tyre_service_tag"
    _description = "tyre service tag model"

    name=fields.Char(string="Name",required=True)
        