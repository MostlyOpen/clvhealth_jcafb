#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from __future__ import print_function

from odoo_api import *


def address_mng_import_from_person_mng(client, batch_name, state):

    tag_id_ZonaRural = tag_get_id(
        client,
        'Zona Rural',
        'Pessoa residente na Zona Rural.')
    tag_id_ZonaUrbana = tag_get_id(
        client,
        'Zona Urbana',
        'Pessoa residente na Zona Urbana.')

    person_mng_model = client.model('myo.person.mng')
    address_mng_model = client.model('myo.address.mng')

    person_mng_browse = person_mng_model.browse([('batch_name', '=', batch_name), ('state', '=', state), ])

    rownum = 0
    duplicated = 0
    imported = 0
    not_imported = 0
    for person_reg in person_mng_browse:

        if (person_reg.street is not False) and (person_reg.street != '') and (person_reg.street != '-'):

            print(rownum, person_reg.street, person_reg.number, person_reg.street2)

            address_mng_browse = address_mng_model.browse([('street', '=', person_reg.street),
                                                           ('number', '=', person_reg.number),
                                                           ('street2', '=', person_reg.street2), ])
            if address_mng_browse.id != []:

                values = {
                    "address_mng_id": address_mng_browse.id[0],
                }
                person_mng_model.write(person_reg.id, values)

                duplicated += 1
            else:

                name = person_reg.street
                if person_reg.number is not False:
                    name = name + ', ' + person_reg.number
                if person_reg.street2 is not False:
                    name = name + ' - ' + person_reg.street2

                tag_ids = []
                if tag_id_ZonaRural in person_reg.tag_ids.id:
                    tag_ids = tag_ids + [(4, tag_id_ZonaRural)]
                if tag_id_ZonaUrbana in person_reg.tag_ids.id:
                    tag_ids = tag_ids + [(4, tag_id_ZonaUrbana)]

                values = {
                    'batch_name': batch_name,
                    'name': name,
                    'code': False,
                    'zip': person_reg.zip,
                    'street': person_reg.street,
                    'number': person_reg.number,
                    'street2': person_reg.street2,
                    'district': person_reg.district,
                    'country_id': person_reg.country_id,
                    'state_id': person_reg.state_id,
                    'l10n_br_city_id': person_reg.l10n_br_city_id,
                    'phone': person_reg.phone,
                    'mobile': person_reg.mobile,
                    'tag_ids': tag_ids,
                }
                address_mng_reg_new = address_mng_model.create(values)

                values = {
                    "address_mng_id": address_mng_reg_new.id,
                }
                person_mng_model.write(person_reg.id, values)

                imported += 1

        else:
            not_imported += 1
        rownum += 1

    print()
    print('--> rownum: ', rownum - 1)
    print('--> duplicated: ', duplicated)
    print('--> imported: ', imported)
    print('--> not_imported: ', not_imported)


def address_mng_export_sqlite(client, args, db_path, table_name):

    conn = sqlite3.connect(db_path)
    conn.text_factory = str

    cursor = conn.cursor()
    try:
        cursor.execute('''DROP TABLE ''' + table_name + ''';''')
    except Exception as e:
        print('------->', e)
    cursor.execute(
        '''
        CREATE TABLE ''' + table_name + ''' (
            id INTEGER NOT NULL PRIMARY KEY,
            name,
            code,
            batch_name,
            tag_ids,
            zip,
            country_id,
            state_id,
            l10n_br_city_id,
            street,
            number,
            street2,
            district,
            phone,
            mobile,
            state,
            notes,
            address_id,
            new_id INTEGER
            );
        '''
    )

    address_mng_model = client.model('myo.address.mng')
    address_mng_browse = address_mng_model.browse(args)

    address_mng_count = 0
    for address_mng_reg in address_mng_browse:
        address_mng_count += 1

        print(address_mng_count, address_mng_reg.id, address_mng_reg.code, address_mng_reg.name.encode("utf-8"))

        address_id = False
        if address_mng_reg.address_id is not False:
            address_id = address_mng_reg.address_id.id

        cursor.execute('''
            INSERT INTO ''' + table_name + '''(
                id,
                name,
                code,
                batch_name,
                tag_ids,
                zip,
                country_id,
                state_id,
                l10n_br_city_id,
                street,
                number,
                street2,
                district,
                phone,
                mobile,
                state,
                notes,
                address_id
                )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (address_mng_reg.id,
                  address_mng_reg.name,
                  address_mng_reg.code,
                  address_mng_reg.batch_name,
                  str(address_mng_reg.tag_ids.id),
                  address_mng_reg.zip,
                  address_mng_reg.country_id.id,
                  address_mng_reg.state_id.id,
                  address_mng_reg.l10n_br_city_id.id,
                  address_mng_reg.street,
                  address_mng_reg.number,
                  address_mng_reg.street2,
                  address_mng_reg.district,
                  address_mng_reg.phone,
                  address_mng_reg.mobile,
                  address_mng_reg.state,
                  address_mng_reg.notes,
                  address_id,
                  )
        )

    conn.commit()
    conn.close()

    print()
    print('--> address_mng_count: ', address_mng_count)


def address_mng_import_sqlite(client, args, db_path, table_name, tag_table_name, address_table_name):

    conn = sqlite3.connect(db_path)
    conn.text_factory = str

    cursor = conn.cursor()

    cursor2 = conn.cursor()

    address_mng_count = 0

    try:
        data = cursor.execute(
            '''
            SELECT
                id,
                name,
                code,
                batch_name,
                tag_ids,
                zip,
                country_id,
                state_id,
                l10n_br_city_id,
                street,
                number,
                street2,
                district,
                phone,
                mobile,
                state,
                notes,
                address_id,
                new_id
            FROM ''' + table_name + ''';
            '''
        )

        address_mng_model = client.model('myo.address.mng')

        print(data)
        print([field[0] for field in cursor.description])
        for row in cursor:
            address_mng_count += 1

            print(address_mng_count, row[0], row[1], row[2], row[3])

            values = {
                'name': row[1],
                'code': row[2],
                'batch_name': row[3],
                # 'tag_ids': row[4],
                'zip': row[5],
                'country_id': row[6],
                'state_id': row[7],
                'l10n_br_city_id': row[8],
                'street': row[9],
                'number': row[10],
                'street2': row[11],
                'district': row[12],
                'phone': row[13],
                'mobile': row[14],
                'state': row[15],
                'notes': row[16],
                'address_id': row[17]
            }
            address_mng_id = address_mng_model.create(values).id

            cursor2.execute(
                '''
               UPDATE ''' + table_name + '''
               SET new_id = ?
               WHERE id = ?;''',
                (address_mng_id,
                 row[0]
                 )
            )

            if row[4] != '[]':

                tag_ids = row[4].split(',')
                new_tag_ids = []
                for x in range(0, len(tag_ids)):
                    tag_id = int(re.sub('[^0-9]', '', tag_ids[x]))
                    cursor2.execute(
                        '''
                        SELECT new_id
                        FROM ''' + tag_table_name + '''
                        WHERE id = ?;''',
                        (tag_id,
                         )
                    )
                    new_tag_id = cursor2.fetchone()[0]

                    values = {
                        'tag_ids': [(4, new_tag_id)],
                    }
                    address_mng_model.write(address_mng_id, values)

                    new_tag_ids.append(new_tag_id)

                print('>>>>>', row[4], new_tag_ids)

            if row[17] != 0:

                address_id = row[17]

                cursor2.execute(
                    '''
                    SELECT new_id
                    FROM ''' + address_table_name + '''
                    WHERE id = ?;''',
                    (address_id,
                     )
                )
                address_id = cursor2.fetchone()[0]

                values = {
                    'address_id': address_id,
                }
                address_mng_model.write(address_mng_id, values)

                print('>>>>>', row[17], address_id)

    except Exception as e:
        print('>>>>>', e)

    conn.commit()
    conn.close()

    print()
    print('--> address_mng_count: ', address_mng_count)
