# -*- coding: utf-8 -*-
from odoo import fields, models

class create_order(models.Model):
    _name = "create.order"
    _description = "create order model"

    name=fields.Char(string="Name",required=True)