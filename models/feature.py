# feature.py
from odoo import models, fields

class RoomFeature(models.Model):
    _name = 'hotel.room.feature'
    _description = 'Room Feature'

    name = fields.Char('Tên đặc điểm phòng', required=True)
