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
    print('--> person_mng_model.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)

    # zip_code = '17455-000'
    # print('-->', client, zip_code)
    # print('--> Executing search_by_cep()...')
    # search_by_cep(client, zip_code)

    # file_name = 'data/JCAFB_2017_Dados_Fernao.csv'
    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # print('-->', client, file_name, batch_name)
    # print('--> Executing person_mng_model_import()...')
    # person_mng_model_import(client, file_name, batch_name)

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'draft'
    # print('-->', client, batch_name, state)
    # print('--> Executing address_mng_import_from_person_mng()...')
    # address_mng_import_from_person_mng(client, batch_name, state)

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'draft'
    # print('-->', client, batch_name, state)
    # print('--> Executing address_mng_create_address()...')
    # address_mng_create_address(client, batch_name, state)

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'revised'
    # print('-->', client, batch_name, state)
    # print('--> Executing person_mng_search_address()...')
    # person_mng_search_address(client, batch_name, state)

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'revised'
    # print('-->', client, batch_name, state)
    # print('--> Executing person_mng_create_person()...')
    # person_mng_create_person(client, batch_name, state)

    print()
    print('--> person_mng_model.py', '- Execution time:', secondsToStr(time() - start))
    print()
