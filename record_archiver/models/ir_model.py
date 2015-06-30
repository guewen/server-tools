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


class IrModel(orm.Model):
    _inherit = 'ir.model'

    def _compute_has_an_active_field(self, cr, uid, ids, name,
                                     args, context=None):
        res = {}
        for model_id in ids:
            active_field_ids = self.pool['ir.model.fields'].search(
                cr, uid,
                [('model_id', '=', model_id),
                 ('name', '=', 'active'),
                 ],
                limit=1,
                context=context)
            res[model_id] = bool(active_field_ids)
        return res

    def _get_from_field(self, cr, uid, ids, context=None):
        this = self.pool['ir.model.fields']
        model_fields = this.read(cr, uid, ids, ['model_id'],
                                 load='_classic_write', context=context)
        return [field['model_id'] for field in model_fields]

    _columns = {
        'has_an_active_field': fields.function(
            _compute_has_an_active_field,
            string='Has an active field',
            readonly=True,
            type='boolean',
            store={
                'ir.model.fields': (_get_from_field, ['model_id', 'name'], 10),
            },
        ),
    }
