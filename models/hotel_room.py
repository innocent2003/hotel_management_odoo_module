from odoo import models, fields, api
from odoo.exceptions import ValidationError

class HotelRoom(models.Model):
    _name = "session7.hotel.room"
    _description = "Hotel Room"

    name = fields.Char(string="Room Name", required=True)
    price = fields.Float(string="Price", required=True)
    is_available = fields.Boolean(string="Available", default=True)

    @api.constrains('price')
    def _check_price(self):
        for record in self:
            if record.price < 0:
                raise ValidationError("Price must be positive.")

    def get_room_details(self, room_id):
        """
        Fetch room details using Odoo ORM.
        """
        room = self.env['session7.hotel.room'].browse(room_id)
        if not room.exists():
            raise ValueError("Room not found!")
        return {
            'name': room.name,
            'price': room.price,
            'is_available': room.is_available,
        }
