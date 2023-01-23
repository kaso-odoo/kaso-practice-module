# -*- coding: utf-8 -*-
from dateutil.relativedelta import relativedelta
from odoo import models, fields

class tyre_retreading_appointment(models.Model):
	_name = 'tyre.retreading.appointment'
	_description = 'tyre retreading model '

	name = fields.Char(string='Name',required=True)
	address = fields.Text(string='Address',required=True)
	postcode = fields.Char(string='Postcode')
	contact_no = fields.Char(string='Contact no.',required=True,copy=False)
	date_availability = fields.Date(string='Available From', default=fields.Date.today()+relativedelta(days=+5), copy=False)
	vehicle_type =  fields.Selection([
        ('car', 'Car'),
        ('tractor', 'Tractor'),
        ('truck', 'Truck'),], string='Vehicle Type',required=True)
	tyre_brand = fields.Text(string='Tyre Brand')
	section_width = fields.Integer(string='Section width (mm)')
	aspect_ratio = fields.Integer(string='Aspect Ratio')
	rim_diameter = fields.Integer(string='Rim Diameter (inch)')
	speed_rating = fields.Char(string='Speed Rating')
	# price = fields.




	



