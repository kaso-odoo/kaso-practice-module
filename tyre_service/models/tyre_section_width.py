# -*- coding: utf-8 -*-
from odoo import fields, models, api


class tyre_section_width(models.Model):
    _name = "tyre.section.width"
    _description = "section width values model"

    values = fields.Integer()

    