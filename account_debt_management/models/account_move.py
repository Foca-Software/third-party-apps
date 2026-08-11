from odoo import models, fields

class AccountMove(models.Model):
    _inherit = "account.move"

    debo_payment_type = fields.Selection(
        selection=[
            ("immediate", "Immediate"),
            ("checking_account", "Checking Account"),
        ],
        string="Payment Type",
        required=True,
        default="immediate",
        tracking=True,
    )