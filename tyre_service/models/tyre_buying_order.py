# -*- coding: utf-8 -*-
from odoo import models, fields

class tyre_buying_order(models.Model):
	_name = 'tyre.buying.order'
	_description = 'tyre buying model '

	name = fields.Char(string='Name',required=True)
	address = fields.Text(string='Address',required=True)
	postcode = fields.Char(string='Postcode')
	contact_no = fields.Char(string='Contact no.',required=True,copy=False)
	vehicle_type =  fields.Selection([
	    ('bike','Bike'),
        ('car', 'Car'),
        ('tractor', 'Tractor'),
        ('truck', 'Truck'),], string='Vehicle Type',required=True)
	tyre_brand = fields.Char(string='Tyre Brand',required=True)
	section_width = fields.Integer(string='Section width(mm)',required=True)
	aspect_ratio = fields.Integer(string='Aspect Ratio',required=True)
	rim_diameter = fields.Integer(string='Rim Diameter(inch)',required=True)
	speed_rating = fields.Char(string='Speed Rating')
	tyre_type = fields.Selection([('tube_type','Tube type'),('tubeless','Tubeless')])
	# create_order_ids = fields.One2many(comodel='create.order','customer_id')
	# price = fields.
	# tyre_sizes = Many2one




	



