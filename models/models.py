# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class /mnt/extra-addons/basic_ecommerce(models.Model):
#     _name = '/mnt/extra-addons/basic_ecommerce./mnt/extra-addons/basic_ecommerce'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100