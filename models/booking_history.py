from odoo import models, fields

class BookingHistory(models.Model):
    _name = 'hotel.booking.history'
    _description = 'Booking History'

    guest_name = fields.Char(string="Guest Name", required=True)
    hotel_id = fields.Many2one('hotel.management', string="Hotel", required=True)
    room_id = fields.Many2one('hotel.room', string="Room", required=True)
    check_in_date = fields.Date(string="Check-in Date", required=True)
    check_out_date = fields.Date(string="Check-out Date", required=True)
