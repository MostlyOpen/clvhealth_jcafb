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

from address_mng import *
from person_mng import *
from jcafb_2017_users import *


def jcafb_export_sqlite(client, db_path):

    l10n_br_zip_args = []
    table_name = 'l10n_br_zip'
    print('-->', client, l10n_br_zip_args, db_path, table_name)
    print('--> Executing l10n_br_zip_export_sqlite()...')
    print()
    l10n_br_zip_export_sqlite(client, l10n_br_zip_args, db_path, table_name)

    tag_args = []
    table_name = 'myo_tag'
    print('-->', client, tag_args, db_path, table_name)
    print('--> Executing tag_export_sqlite()...')
    print()
    tag_export_sqlite(client, tag_args, db_path, table_name)

    address_category_args = []
    table_name = 'myo_address_category'
    print('-->', client, address_category_args, db_path, table_name)
    print('--> Executing address_category_export_sqlite()...')
    print()
    address_category_export_sqlite(client, address_category_args, db_path, table_name)

    address_args = []
    table_name = 'myo_address'
    print('-->', client, address_args, db_path, table_name)
    print('--> Executing address_export_sqlite()...')
    print()
    address_export_sqlite(client, address_args, db_path, table_name)

    person_category_args = []
    table_name = 'myo_person_category'
    print('-->', client, person_category_args, db_path, table_name)
    print('--> Executing person_category_export_sqlite()...')
    print()
    person_category_export_sqlite(client, person_category_args, db_path, table_name)

    person_args = []
    table_name = 'myo_person'
    print('-->', client, person_args, db_path, table_name)
    print('--> Executing person_export_sqlite()...')
    print()
    person_export_sqlite(client, person_args, db_path, table_name)

    person_address_role_args = []
    table_name = 'myo_person_address_role'
    print('-->', client, person_address_role_args, db_path, table_name)
    print('--> Executing person_address_role_export_sqlite()...')
    print()
    person_address_role_export_sqlite(client, person_address_role_args, db_path, table_name)

    person_address_args = []
    table_name = 'myo_person_address'
    print('-->', client, person_address_args, db_path, table_name)
    print('--> Executing person_address_export_sqlite()...')
    print()
    person_address_export_sqlite(client, person_address_args, db_path, table_name)

    address_mng_args = []
    table_name = 'myo_address_mng'
    print('-->', client, address_mng_args, db_path, table_name)
    print('--> Executing address_mng_export_sqlite()...')
    print()
    address_mng_export_sqlite(client, address_mng_args, db_path, table_name)

    person_mng_args = []
    table_name = 'myo_person_mng'
    print('-->', client, person_mng_args, db_path, table_name)
    print('--> Executing person_mng_export_sqlite()...')
    print()
    person_mng_export_sqlite(client, person_mng_args, db_path, table_name)


def jcafb_import_sqlite(client, db_path):

    l10n_br_zip_args = []
    table_name = 'l10n_br_zip'
    print('-->', client, l10n_br_zip_args, db_path, table_name)
    print('--> Executing l10n_br_zip_import_sqlite()...')
    print()
    l10n_br_zip_import_sqlite(client, l10n_br_zip_args, db_path, table_name)

    tag_args = []
    table_name = 'myo_tag'
    print('-->', client, tag_args, db_path, table_name)
    print('--> Executing tag_import_sqlite()...')
    print()
    tag_import_sqlite(client, tag_args, db_path, table_name)

    address_args = []
    table_name = 'myo_address'
    tag_table_name = 'myo_tag'
    print('-->', client, address_args, db_path, table_name, tag_table_name)
    print('--> Executing address_import_sqlite()...')
    print()
    address_import_sqlite(client, address_args, db_path, table_name, tag_table_name)

    address_mng_args = []
    table_name = 'myo_address_mng'
    tag_table_name = 'myo_tag'
    address_table_name = 'myo_address'
    print('-->', client, address_mng_args, db_path, table_name, tag_table_name, address_table_name)
    print('--> Executing address_mng_import_sqlite()...')
    print()
    address_mng_import_sqlite(client, address_mng_args, db_path, table_name, tag_table_name, address_table_name)

    person_mng_args = []
    table_name = 'myo_person_mng'
    tag_table_name = 'myo_tag'
    address_mng_table_name = 'myo_address_mng'
    address_table_name = 'myo_address'
    print(
        '-->', client, person_mng_args, db_path,
        table_name, tag_table_name, address_mng_table_name, address_table_name
    )
    print('--> Executing person_mng_import_sqlite()...')
    print()
    person_mng_import_sqlite(
        client, person_mng_args, db_path,
        table_name, tag_table_name, address_mng_table_name, address_table_name
    )


def get_arguments():

    global server
    global username
    global password
    global dbname
    global db_server
    global db_user
    global db_password

    parser = argparse.ArgumentParser()
    parser.add_argument('--server', action="store", dest="server")
    parser.add_argument('--user', action="store", dest="username")
    parser.add_argument('--pw', action="store", dest="password")
    parser.add_argument('--db', action="store", dest="dbname")
    parser.add_argument('--dbserver', action="store", dest="db_server")
    parser.add_argument('--dbu', action="store", dest="db_user")
    parser.add_argument('--dbw', action="store", dest="db_password")

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

    if args.db_server is not None:
        db_server = args.db_server
    elif db_server == '*':
        db_server = getpass.getpass('db_server: ')

    if args.db_user is not None:
        db_user = args.db_user
    elif db_user == '*':
        db_user = getpass.getpass('db_user: ')

    if args.db_password is not None:
        db_password = args.db_password
    elif db_password == '*':
        db_password = getpass.getpass('db_password: ')


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

    db_server = 'localhost'
    # db_server = '*'

    db_user = 'openerp'
    # db_user = '*'

    db_password = 'openerp'
    # db_password = '*'

    print()
    print('--> setup.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)

    # ***** 2016-09-08 *****
    #

    # zip_code = '17455-000'
    # print('-->', client, zip_code)
    # print('--> Executing search_by_cep()...')
    # search_by_cep(client, zip_code)

    # file_name = 'data/JCAFB_2017_Dados_Fernao.csv'
    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # print('-->', client, file_name, batch_name)
    # print('--> Executing person_mng_import()...')
    # person_mng_import(client, file_name, batch_name)

    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # ***** 2016-09-15 *****
    #

    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # ***** 2016-10-04 *****
    #

    # db_path = 'data/clvhealth_jcafb_2017_2016-09-15.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-04a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-04a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'revised'
    # print('-->', client, batch_name, state)
    # print('--> Executing address_mng_import_from_person_mng()...')
    # address_mng_import_from_person_mng(client, batch_name, state)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-04b.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-04b.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # ***** 2016-10-05 *****
    #

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-05a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-05b.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-05b.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'waiting'
    # print('-->', client, batch_name, state)
    # print('--> Executing address_mng_create_address()...')
    # address_mng_create_address(client, batch_name, state)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-05c.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-05c.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'revised'
    # print('-->', client, batch_name, state)
    # print('--> Executing person_mng_search_address()...')
    # person_mng_search_address(client, batch_name, state)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-05d.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-05d.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-05e.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # ***** 2016-10-06 *****
    #

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'waiting'
    # print('-->', client, batch_name, state)
    # print('--> Executing person_mng_create_person()...')
    # person_mng_create_person(client, batch_name, state)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-06a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # ***** 2016-10-?? *****
    #

    # res_partner_args = []
    # db_path = 'data/clvhealth_jcafb_2017_test.sqlite'
    # table_name = 'res_partner'
    # print('-->', client, res_partner_args, db_path, table_name)
    # print('--> Executing res_partner_export_sqlite()...')
    # print()
    # res_partner_export_sqlite(client, res_partner_args, db_path, table_name)

    # conn_string = "dbname='" + dbname + "' user='" + db_user + "' host='" + db_server + \
    #               "' password='" + db_password + "'"
    # res_users_args = []
    # db_path = 'data/clvhealth_jcafb_2017_test.sqlite'
    # table_name = 'res_users'
    # print('-->', client, res_users_args, db_path, table_name, conn_string)
    # print('--> Executing res_users_export_sqlite()...')
    # print()
    # res_users_export_sqlite(client, res_users_args, db_path, table_name, conn_string)

    print()
    print('--> setup.py', '- Execution time:', secondsToStr(time() - start))
    print()
