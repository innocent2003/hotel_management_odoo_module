# room.py
from odoo import models, fields
from datetime import datetime, timedelta
import logging

_logger = logging.getLogger(__name__)
class Room(models.Model):
    _name = 'hotel.room'
    _description = 'Room Management'

    name = fields.Char('Mã phòng', required=True)
    hotel_id = fields.Many2one('hotel.management', string='Khách sạn', required=True)
    address = fields.Char('Địa chỉ khách sạn', related='hotel_id.address', store=True)
    bed_type = fields.Selection([('single', 'Giường đơn'), ('double', 'Giường đôi')], string='Loại giường', required=True)
    price = fields.Float('Giá phòng')
    feature_ids = fields.Many2many('hotel.room.feature', 'room_feature_rel', 'room_id', 'feature_id', string='Đặc điểm phòng')
    state = fields.Selection([('available', 'Trống'), ('booked', 'Đã đặt')], string='Trạng thái phòng', default='available')
    last_reservation_date = fields.Date('Last Reservation Date', help='The last date this room was reserved')

    _sql_constraints = [
        ('unique_room_code', 'unique(name, hotel_id)', 'Mã phòng phải là duy nhất trong một khách sạn!')
    ]

    @api.model
    def check_unreserved_rooms(self):
        seven_days_ago = fields.Date.to_date(fields.Date.today()) - timedelta(days=7)
        unreserved_rooms = self.search([
            ('last_reservation_date', '<=', seven_days_ago),
            '|', ('last_reservation_date', '=', False), ('state', '=', 'available')
        ])
        for room in unreserved_rooms:
            _logger.info(f"Room: {room.name}, Hotel: {room.hotel_id.name}")