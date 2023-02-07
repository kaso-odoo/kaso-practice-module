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
    # tyre_brand
    tyre_brandb = fields.Selection([
        ('tvs', 'TVS'),('ralco','Ralco'),('ceat', 'Ceat')],string='Tyre BrandB')
    tyre_brandc = fields.Selection([
        ('ceat', 'Ceat'),('apollo', 'Apollo'),('michelin', 'Michelin')],string='Tyre BrandC')
    tyre_brandtr = fields.Selection([
        ('mrf', 'MRF'),('jktyre','JKtyre'),('apollo', 'Apollo')],string='Tyre BrandTR')
    tyre_brandt = fields.Selection([
        ('jktyre','JKtyre'),('bkt','BKT')],string='Tyre BrandT')
    # section_width
    section_widthb = fields.Selection([
        ('70','70'),('80','80'),('90','90'),('100','100'),('110','110')],string='Section width(mm)',required=True)
    section_widthc = fields.Selection([
        ('155','155'),('165','165'),('175','175'),('185','185'),('195','195'),('195','195')],string='Section width(mm)',required=True)
    section_widthtr = fields.Selection([
        ('235','225'),('245','245'),('255','255'),('260','260'),('270','270')],string='Section width(mm)',required=True)
    section_widtht = fields.Selection([
        ('280','280'),('320','320'),('340','340'),('380','380'),('420','420')],string='Section width(mm)',required=True)
    section_width_id = fields.Many2one('tyre_section_width',string='section_width')
    aspect_ratio = fields.Integer(string='Aspect Ratio',compute='_compute_aspect_ratio', required=True,readonly=False,store=True)
    rim_diameter = fields.Integer(string='Rim Diameter(inch)', required=True)
    speed_rating = fields.Char(string='Speed Rating')
    tyre_type = fields.Selection(
        [('tube_type', 'Tube type'),('tubeless', 'Tubeless')])
    price = fields.Integer(
        string='Price', compute='_compute_price', store=True,required=True)
    customer_id = fields.Many2one('tyre.buying.order', required=True)
    quantity = fields.Integer(string='Quantity')

    @api.depends('section_widthb', 'aspect_ratio', 'rim_diameter', 'quantity')
    def _compute_price(self):
        for record in self:
            if record.vehicle_type == 'bike':
                record.price = (
                    ((int(record.section_widthb)*record.aspect_ratio*record.rim_diameter)/100)*2)*record.quantity
            elif record.vehicle_type == 'car':
                record.price = (
                    ((int(record.section_widthc)*record.aspect_ratio*record.rim_diameter)/100)*2)*record.quantity
            elif record.vehicle_type == 'truck':
                record.price = (
                    ((int(record.section_widthtr)*record.aspect_ratio*record.rim_diameter)/100)*2)*record.quantity
            elif record.vehicle_type == 'tractor':
                record.price = (
                    ((int(record.section_widtht)*record.aspect_ratio*record.rim_diameter)/100)*2)*record.quantity
            else:
                return True

    @api.depends('vehicle_type')
    def _compute_aspect_ratio(self):
        for record in self:
            if record.vehicle_type == 'tractor':
                record.aspect_ratio = '85'
            else:
                record.aspect_ratio = ''

