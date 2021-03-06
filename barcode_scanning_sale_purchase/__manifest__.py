# -*- coding: utf-8 -*-
#############################################################################
#
#    Cybrosys Technologies Pvt. Ltd.
#
#    Copyright (C) 2019-TODAY Cybrosys Technologies(<https://www.cybrosys.com>).
#    Author: Sreejith P (odoo@cybrosys.com)
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': 'Barcode scanning support for sale and Purchase',
    'version': '13.0.1.0.0',
    'category': 'Sales',
    'summary': 'This module will help you to use barcode scanner in sales',
    'author': 'Proadvisory Business Solution',
    'website': 'http://www.proadvisory.com',
    'depends': ['purchase', 'sale_management', 'pabs_sale', 'barcodes'],
    'demo': [],
    'data': [
        'views/sale_order_line.xml',
        'views/purchase_order_line.xml',
        'views/barcode_scanning.xml',
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'qweb': [],
}
