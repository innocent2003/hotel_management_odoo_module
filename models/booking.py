from odoo import models, fields

class Booking(models.Model):
    _name = 'booking'
    _description = 'Booking'

    name = fields.Char(string="Booking Reference", required=True)
    customer_name = fields.Char(string="Customer Name", required=True)
    room_id = fields.Many2one('room', string="Room", required=True)
    check_in_date = fields.Date(string="Check-In Date", required=True)
    check_out_date = fields.Date(string="Check-Out Date", required=True)
