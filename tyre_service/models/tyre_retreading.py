# -*- coding: utf-8 -*-

from odoo import models, fields

class tyre_retreading(models.Model):
	_name = 'tyre.retreading'
	_description = 'tyre retreading model '

	name = fields.Char(string='Name',required=True)
	address = fields.text(string='Address',required=True)
	contact_no = fields.Integer(string='Contact no.',required=True,copy=False)
	vehical_type =  fields.Selection([
        ('cars', 'Cars'),
        ('bikes', 'Bikes'),
        ('tractor', 'Tractor'),
        ('trucks', 'Trucks'),], string='Vehicle Type',required=True)
	tyre_brand = 
	rim_size = 
	



	



