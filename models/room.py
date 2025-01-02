# room.py
from odoo import models, fields

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

    _sql_constraints = [
        ('unique_room_code', 'unique(name, hotel_id)', 'Mã phòng phải là duy nhất trong một khách sạn!')
    ]
