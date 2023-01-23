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
	tyre_brand = fields.Text(string='Tyre Brand')
	section_width = fields.Integer(string='Section width(mm)')
	aspect_ratio = fields.Integer(string='Aspect Ratio')
	rim_diameter = fields.Integer(string='Rim Diameter(inch)')
	speed_rating = fields.Char(string='Speed Rating')
	# price = fields.




	



