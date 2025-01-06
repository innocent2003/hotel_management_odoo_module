from odoo import models, fields

class Room(models.Model):
    _name = 'room'
    _description = 'Room'

    name = fields.Char(string="Room Name", required=True)
    hotel_id = fields.Many2one('hotel', string="Hotel")
    features = fields.Text(string="Features")
