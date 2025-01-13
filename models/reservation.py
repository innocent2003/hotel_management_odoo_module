# reservation.py
from odoo import models, fields, api
from odoo.exceptions import UserError
from datetime import datetime

class Reservation(models.Model):
    _name = 'hotel.reservation'
    _description = 'Room Reservation'

    name = fields.Char('Mã đặt phòng', required=True)
    customer_name = fields.Char('Tên người đặt', required=True)
    reservation_date = fields.Date('Ngày đặt', default=fields.Date.context_today)
    hotel_id = fields.Many2one('hotel.management', string='Khách sạn', required=True)
    room_id = fields.Many2one('hotel.room', string='Mã phòng', domain="[('hotel_id', '=', hotel_id), ('state', '=', 'available')]", required=True)
    check_in_date = fields.Date('Ngày nhận phòng', required=True)
    check_out_date = fields.Date('Ngày trả phòng', required=True)
    state = fields.Selection([('new', 'Mới'), ('booked', 'Đã đặt')], string='Trạng thái đặt', default='new')

    @api.constrains('check_in_date', 'check_out_date')
    def _check_dates(self):
        for record in self:
            if record.check_in_date > record.check_out_date:
                raise ValidationError('Ngày nhận phòng không được lớn hơn ngày trả phòng.')

    def action_approve(self):
        if not self:
            raise UserError('No records selected for approval.')

        for record in self:
            if record.state != 'new':
                raise UserError(f'Record {record.name} is not in "New" state and cannot be approved.')
            record.write({'state': 'booked'})