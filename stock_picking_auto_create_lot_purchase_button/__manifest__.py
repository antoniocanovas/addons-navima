##############################################################################
#
#    Punt Sistemes SL
#    Copyright (C) 2024 - Punt Sistemes (http://www.puntsistemes.es).
#    All Rights Reserved
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
    "name": "Stock picking auto lot purchase button",
    "version": "18.0",
    "depends": [
        "product",
        "stock",
        # OCA:
        "stock_picking_auto_create_lot",
    ],
    "author": "Punt Sistemes",
    "category": "Stock",
    "website": "https://www.puntsistemes.es",
    "description": """
        Based on OCA module stock_picking_auto_create_lot, adds a button on stock picking RECEIPTS to create
        manually purchase LOTS. It will be used to send to manufacturer this information and will back pasted
        on received products.
    """,
    "data": [
        "views/stock_picking_views.xml",
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}
