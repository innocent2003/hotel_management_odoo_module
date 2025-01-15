from odoo import models, fields, api

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    x_discount = fields.Monetary(string="Discount", currency_field='currency_id', default=0.0, help="Direct discount applied to the unit price.")

    @api.depends('product_uom_qty', 'discount', 'price_unit', 'tax_id', 'x_discount')
    def _compute_amount(self):
        """
        Compute the amounts of the SO line, taking into account the discount.
        """
        for line in self:
            # Adjust the unit price by subtracting the discount
            discounted_price_unit = line.price_unit - line.x_discount
            # Calculate the subtotal before tax
            line.price_subtotal = discounted_price_unit * line.product_uom_qty
            # Compute taxes
            taxes = line.tax_id.compute_all(discounted_price_unit, line.order_id.currency_id, line.product_uom_qty, product=line.product_id, partner=line.order_id.partner_id)
            # Set the totals
            line.price_tax = sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))
            line.price_total = taxes['total_included']
            line.price_subtotal = taxes['total_excluded']
