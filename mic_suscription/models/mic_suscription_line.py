# coding=utf-8
import dp as dp

from odoo import api, models, fields


class SucriptionMic(models.Model):
    _inherit = 'sale.subscription.line'
    abonado2 = fields.Float(string=u"Abonado")
    partner_abonado = fields.Boolean(related='analytic_account_id.partner_abonado')

    @api.depends('price_unit', 'quantity', 'discount', 'analytic_account_id.pricelist_id', 'abonado')
    def _compute_price_subtotal(self):
        for line in self:
            line_sudo = line.sudo()
            price = line.env['account.tax']._fix_tax_included_price(line.price_unit, line_sudo.product_id.taxes_id,
                                                                    [])
            line.price_subtotal = line.quantity * (line.partner_abonado and line.abonado or 1.0) * price
            if line.analytic_account_id.pricelist_id:
                line.price_subtotal = line_sudo.analytic_account_id.pricelist_id.currency_id.round(
                    line.price_subtotal)
