# -*- coding: utf-8 -*-
from odoo import fields, models, api


class create_order(models.Model):
    _name = "create.order"
    _description = "create order model"

    # name = fields.Char(string="Name", required=True)
    vehicle_type = fields.Selection([
        ('bike', 'Bike'),
        ('car', 'Car'),
        ('tractor', 'Tractor'),
        ('truck', 'Truck'),], string='Vehicle Type', required=True)
    tyre_brandb = fields.Selection([
        ('tvs', 'TVS'),('ralco','Ralco'),('ceat', 'Ceat')],string='Tyre BrandB')
    tyre_brandc = fields.Selection([
        ('ceat', 'Ceat'),('apollo', 'Apollo'),('michelin', 'Michelin')],string='Tyre BrandC')
    tyre_brandtr = fields.Selection([
        ('mrf', 'MRF'),('jktyre','JKtyre'),('apollo', 'Apollo')],string='Tyre BrandTR')
    tyre_brandt = fields.Selection([
        ('jktyre','JKtyre'),('bkt','BKT')],string='Tyre BrandT')
    
    section_width = fields.Integer(string='Section width(mm)', required=True)
    aspect_ratio = fields.Integer(string='Aspect Ratio', required=True)
    rim_diameter = fields.Integer(string='Rim Diameter(inch)', required=True)
    speed_rating = fields.Char(string='Speed Rating')
    tyre_type = fields.Selection(
        [('tube_type', 'Tube type'), ('tubeless', 'Tubeless')])
    price = fields.Integer(
        string='Price', compute='_compute_price', store=True)
    customer_id = fields.Many2one('tyre.buying.order', required=True)
    quantity = fields.Integer(string='Quantity')

    @api.depends('section_width', 'aspect_ratio', 'rim_diameter', 'quantity')
    def _compute_price(self):
        for record in self:
            record.price = (
                ((record.section_width*record.aspect_ratio*record.rim_diameter)/100)*2)*record.quantity
        return True

    @api.depends('vehicle_type')
    def _compute_tyre_brand(self):
        for record in self:
            if self.vehicle_type == 'Bike':
                self.tyre_brand = [('tvs', 'TVS'),('ralco','Ralco'),('ceat', 'Ceat')]
            elif self.vehicle_type == 'Car':
                self.tyre_brand = [('ceat', 'Ceat'),('apollo','Apollo'),('michelin','Michelin')]
            elif self.vehicle_type == 'Truck':
                self.tyre_brand = [('mrf','MRF'),('apollo','Apollo'),('jktyre', 'JKtyre')]
            elif self.vehicle_type == 'Tractor':
                self.tyre_brand = [('bkt', 'BKT'),('mrf','MRF')]
