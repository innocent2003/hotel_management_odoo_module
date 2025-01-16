from odoo import models, fields, api
from datetime import timedelta

class HotelInvoice(models.Model):
    _inherit = 'account.move'

    room_id = fields.Many2one('hotel.room', string="Room", help="Room rented by the customer")
    check_in_date = fields.Datetime(string="Check-In Date", required=True)
    check_out_date = fields.Datetime(string="Check-Out Date", required=True)
    total_nights = fields.Integer(string="Total Nights", compute='_compute_total_nights', store=True)
    room_rate = fields.Monetary(string="Room Rate", related='room_id.rate', readonly=True)
    total_amount = fields.Monetary(string="Total Amount", compute='_compute_total_amount', store=True)

    @api.depends('check_in_date', 'check_out_date')
    def _compute_total_nights(self):
        for record in self:
            if record.check_in_date and record.check_out_date:
                delta = record.check_out_date - record.check_in_date
                record.total_nights = delta.days if delta.days > 0 else 1
            else:
                record.total_nights = 0

    @api.depends('total_nights', 'room_rate')
    def _compute_total_amount(self):
        for record in self:
            record.total_amount = record.total_nights * record.room_rate
