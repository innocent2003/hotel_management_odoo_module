from odoo import models, fields

class Hotel(models.Model):
    _name = 'hotel'
    _description = 'Hotel'

    name = fields.Char(string="Hotel Name", required=True)
    description = fields.Text(string="Description")
