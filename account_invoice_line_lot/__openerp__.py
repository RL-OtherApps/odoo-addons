# -*- coding: utf-8 -*-
##############################################################################
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
    "name": "Invoice Line Lots",
    "version": "8.0.0.1.0",
    'category': 'Generic Modules/Accounting',
    "depends": [
        "sale_stock",
        "stock_account"],
    "author": "AvanzOSC",
    "summary": "Display delivered serial numbers in invoice lines",
    'website': 'http://www.avanzosc.es',
    'data': ['views/invoice_view.xml',
             'views/report_invoice_view.xml'],
    'installable': True,
}
