# -*- coding: utf-8 -*-
##############################################################################
#
#    Punt Sistemes SL
#    Copyright (C) 2024 - Punt Sistemes (http://www.puntsistemes.es). All Rights Reserved
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": 'Custom Navima',
    "version": '1.0',
    "depends": [
        'product',
        'stock',
        'shoes_dealer',
        'shoes_campaign',
    ],
    "author": "Punt Sistemes",
    "category": 'Stock',
    "website": "https://www.puntsistemes.es",
    "description": """
        Custom devs Navima.
    """,
    "data": [
        'views/project_project_views.xml',
        'views/stock_picking_views.xml',
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
