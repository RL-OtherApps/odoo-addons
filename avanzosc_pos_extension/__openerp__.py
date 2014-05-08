
# -*- encoding: utf-8 -*-
##############################################################################
#
#    Avanzosc - Avanced Open Source Consulting
#    Copyright (C) 2011 - 2012 Avanzosc <http://www.avanzosc.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

{
    "name": "AvanzOsc - POS extension",
    "version": "1.0",
    "depends": ["point_of_sale"],
    "author": "AvanzOSC",
    "website" : "http://www.avanzosc.com",
    "category": "Custom Module",
    "description": """
        Este módulo mete 3 campos nuevos al pagar el ticket del terminal del punto de venta.
        Los nuevos campos son el Importe de tickect, Importe que le da el cliente, y calcula 
        las vueltas que hay de devolver.
    """,
    "init_xml": [],
    'update_xml': ["point_of_sale_view.xml",],
    'demo_xml': [],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}