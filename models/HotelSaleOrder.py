from odoo import models, fields, api

class HotelSaleOrder(models.Model):
    _inherit = 'sale.order'

    hotel_id = fields.Many2one('hotel.management', string="Hotel", help="Hotel associated with the sale order")
    room_ids = fields.Many2many('hotel.room', string="Rooms")
    check_in_date = fields.Date(string="Check-in Date")
    check_out_date = fields.Date(string="Check-out Date")
    guest_id = fields.Many2one('res.partner', string="Guest", help="Guest responsible for the sale order")

    def action_create_hotel_invoice(self):
        """
        Generate an invoice from the sale order.
        """
        for order in self:
            invoice_vals = {
                'move_type': 'out_invoice',
                'partner_id': order.partner_id.id,
                'invoice_date': fields.Date.today(),
                'hotel_id': order.hotel_id.id,
                'room_ids': [(6, 0, order.room_ids.ids)],
                'check_in_date': order.check_in_date,
                'check_out_date': order.check_out_date,
                'invoice_line_ids': [(0, 0, {
                    'product_id': line.product_id.id,
                    'quantity': line.product_uom_qty,
                    'price_unit': line.price_unit,
                }) for line in order.order_line]
            }
            self.env['account.move'].create(invoice_vals)
