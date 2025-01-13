# hotel.py
from odoo import models, fields, api

class Hotel(models.Model):
    _name = 'hotel.management'
    _description = 'Hotel Management'

    name = fields.Char('Tên khách sạn', required=True)
    address = fields.Char('Địa chỉ khách sạn')
    floors = fields.Integer('Số tầng')
    room_ids = fields.One2many('hotel.room', 'hotel_id', string='Danh sách phòng')
    room_count = fields.Integer('Số phòng', compute='_compute_room_count')
    user_ids = fields.Many2many('res.users', string='Users')
    manager_id = fields.Many2one('res.users', string='Manager')

    @api.depends('room_ids')
    def _compute_room_count(self):
        for record in self:
            record.room_count = len(record.room_ids)
