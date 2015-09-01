# -*- coding: utf-8 -*-
#
#
#    Authors: Guewen Baconnier
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
#

from openerp.osv import orm, fields


class ElasticSearchViewIndex(orm.Model):
    _name = 'elasticsearch.view.index'
    _description = 'ElasticSearch View Index'

    def _selection_sql_view(self, cr, uid, context=None):
        cr.execute(
            "SELECT viewname FROM pg_catalog.pg_views "
            "WHERE schemaname NOT IN ('pg_catalog', 'information_schema') "
            "ORDER BY schemaname, viewname"
        )
        return [(row[0], row[0]) for row in cr.fetchall()]

    _columns = {
        'name': fields.char(string='Index name', required=True),
        'host_ids': fields.many2many('elasticsearch.host',
                                     string='Hosts',
                                     required=True),
        'sql_view': fields.selection(_selection_sql_view,
                                     string='View',
                                     required=True),
    }
