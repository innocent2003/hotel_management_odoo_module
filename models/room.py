from odoo import models, fields

class HotelRoom(models.Model):
    _inherit = 'hotel.room'

    room_size = fields.Float(string="Room Size (sqm)")
    max_occupancy = fields.Integer(string="Maximum Occupancy")
    smoking_allowed = fields.Selection([
        ('yes', 'Yes'),
        ('no', 'No')
    ], string="Smoking Allowed", default='no')
