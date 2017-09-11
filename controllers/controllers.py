# -*- coding: utf-8 -*-
from odoo import http

# class /mnt/extra-addons/basicEcommerce(http.Controller):
#     @http.route('//mnt/extra-addons/basic_ecommerce//mnt/extra-addons/basic_ecommerce/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/basic_ecommerce//mnt/extra-addons/basic_ecommerce/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/basic_ecommerce.listing', {
#             'root': '//mnt/extra-addons/basic_ecommerce//mnt/extra-addons/basic_ecommerce',
#             'objects': http.request.env['/mnt/extra-addons/basic_ecommerce./mnt/extra-addons/basic_ecommerce'].search([]),
#         })

#     @http.route('//mnt/extra-addons/basic_ecommerce//mnt/extra-addons/basic_ecommerce/objects/<model("/mnt/extra-addons/basic_ecommerce./mnt/extra-addons/basic_ecommerce"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/basic_ecommerce.object', {
#             'object': obj
#         })