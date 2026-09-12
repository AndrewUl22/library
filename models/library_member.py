# -*- coding: utf-8 -*-
from odoo import api, fields, models


class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'
    _order = 'name'

    name = fields.Char(string='Full Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    user_id = fields.Many2one(
        'res.users',
        string='Related User',
        help='Link to a login account, so this member can be '
             'restricted to seeing only their own loans.',
    )

    loan_ids = fields.One2many(
        'library.loan', 'member_id', string='Loans'
    )
    loan_count = fields.Integer(
        string='Active Loans', compute='_compute_loan_count'
    )

    @api.depends('loan_ids.state')
    def _compute_loan_count(self):
        for member in self:
            member.loan_count = len(
                member.loan_ids.filtered(lambda l: l.state == 'ongoing')
            )
