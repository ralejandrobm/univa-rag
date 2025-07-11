from odoo import models, fields


class AiunivaInterestedParty(models.Model):
    _name = "ai_univa.interested.party"
    _description = "Interested Party"

    name = fields.Char(string="Name", required=True)
    active = fields.Boolean(string="Active", default=True)
