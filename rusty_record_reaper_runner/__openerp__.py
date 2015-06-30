# -*- coding: utf-8 -*-
#
#    Author: Yannick Vaucher
#    Copyright 2015 Camptocamp SA
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
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

{'name': 'Rusty Record Reaper Runner',
 'version': '0.1',
 'description': """
 Define a cron job to deactivate old records in order to optimize performances.

 Records are deactivated base on last activity on them (write_date).

 You can configure lifespan of each type of record in
 Settings -> Configuration -> Rusty Record Reaper Runner

 Lifespan is defined per record per company.
 """,
 'author': 'Camptocamp',
 'maintainer': 'Camptocamp',
 'license': 'AGPL-3',
 'category': 'misc',
 'complexity': "easy",  # easy, normal, expert
 'depends': ['base'],
 'website': 'www.camptocamp.com',
 'data': ['views/res_config.xml',
          'data/cron.xml'],
 'test': [],
 'installable': True,
 'auto_install': False,
 }
