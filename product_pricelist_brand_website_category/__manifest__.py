# -*- encoding: utf-8 -*-
##############################################################################
#                                                                            #
#  OpenERP, Open Source Management Solution.                                 #
#                                                                            #
#  @author @author Daikhi Oualid <o_daikhi@esi.dz>                           #
#                                                                            #
#  This program is free software: you can redistribute it and/or modify      #
#  it under the terms of the GNU Affero General Public License as            #
#  published by the Free Software Foundation, either version 3 of the        #
#  License, or (at your option) any later version.                           #
#                                                                            #
#  This program is distributed in the hope that it will be useful,           #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the              #
#  GNU Affero General Public License for more details.                       #
#                                                                            #
#  You should have received a copy of the GNU Affero General Public License  #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.      #
##############################################################################
{
    'name': 'Pricelist Based On Brand and Website Public Category',
    'author': 'Fennec Solutions',
    'version': '10.0.1.0',
    'license': 'AGPL-3',
    'category': 'Product',
    'description': """
      This module will add an option to configure Odoo pricelist Based on Brand or  Website Public Category.
      You may have Problem if you already installed a custom module for Brand, you can just contact me for some changes  <o_daikhi@esi.dz>   
    """,
    'depends': [
        'product',
        'website_sale',
    ],
    'data': [
        'views/product_pricelist_item.xml',
        'views/product_views.xml',
        'security/ir.model.access.csv',
    ],
    'images': ['static/description/Banner.png'],
    'installable': True,
    'auto_install': False,
    'price':20,
    'currency': 'EUR',
    'license': 'OPL-1',
}
