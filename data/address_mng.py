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

import argparse
import getpass
import erppeek

from odoo_api import *


def address_mng_import_from_person_mng(client, batch_name, state):

    tag_id_ZonaRural = myo_tag_get_id(
        client,
        'Zona Rural',
        'Pessoa residente na Zona Rural.')
    tag_id_ZonaUrbana = myo_tag_get_id(
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
                    "state": 'revised',
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
                    'tag_ids': tag_ids,
                }
                address_mng_reg_new = address_mng_model.create(values)

                values = {
                    "address_mng_id": address_mng_reg_new.id,
                    "state": 'revised',
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


def get_arguments():

    global server
    global username
    global password
    global dbname

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', action="store", dest="server")
    parser.add_argument('--user', action="store", dest="username")
    parser.add_argument('--pw', action="store", dest="password")
    parser.add_argument('--db', action="store", dest="dbname")

    args = parser.parse_args()
    print('%s%s' % ('--> ', args))

    if args.server is not None:
        server = args.server
    elif server == '*':
        server = raw_input('server: ')

    if args.dbname is not None:
        dbname = args.dbname
    elif dbname == '*':
        dbname = raw_input('dbname: ')

    if args.username is not None:
        username = args.username
    elif username == '*':
        username = raw_input('username: ')

    if args.password is not None:
        password = args.password
    elif password == '*':
        password = getpass.getpass('password: ')


def secondsToStr(t):

    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


if __name__ == '__main__':

    server = 'http://localhost:8069'
    # server = '*'

    username = 'username'
    # username = '*'
    password = 'password'
    # password = '*'

    dbname = 'odoo'
    # dbname = '*'

    print()
    print('--> addres_mng.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)

    print()
    print('--> addres_mng.py', '- Execution time:', secondsToStr(time() - start))
    print()
