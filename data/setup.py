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
# MERCHANTABILITY or FITNESS1icense for more details.
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
from jcafb_2017_communities import *
from jcafb_2017_residences import *
from jcafb_2017_persons import *
from jcafb_2017_events import *
from jcafb_2017_documents import *
from jcafb_2017_surveys import *


def jcafb_export_sqlite(client, db_path, conn_string):

    res_partner_args = []
    table_name = 'res_partner'
    print('-->', client, res_partner_args, db_path, table_name)
    print('--> Executing res_partner_export_sqlite()...')
    print()
    res_partner_export_sqlite(client, res_partner_args, db_path, table_name)

    res_users_args = []
    table_name = 'res_users'
    print('-->', client, res_users_args, db_path, table_name, conn_string)
    print('--> Executing res_users_export_sqlite()...')
    print()
    res_users_export_sqlite(client, res_users_args, db_path, table_name, conn_string)

    hr_department_args = []
    table_name = 'hr_department'
    print('-->', client, hr_department_args, db_path, table_name)
    print('--> Executing hr_department_export_sqlite()...')
    print()
    hr_department_export_sqlite(client, hr_department_args, db_path, table_name)

    hr_employee_args = []
    table_name = 'hr_employee'
    print('-->', client, hr_employee_args, db_path, table_name)
    print('--> Executing hr_employee_export_sqlite()...')
    print()
    hr_employee_export_sqlite(client, hr_employee_args, db_path, table_name)

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

    person_category_args = []
    table_name = 'myo_address_category'
    print('-->', client, person_category_args, db_path, table_name)
    print('--> Executing address_category_export_sqlite()...')
    print()
    address_category_export_sqlite(client, person_category_args, db_path, table_name)

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

    community_category_args = []
    table_name = 'myo_community_category'
    print('-->', client, community_category_args, db_path, table_name)
    print('--> Executing community_category_export_sqlite()...')
    print()
    community_category_export_sqlite(client, community_category_args, db_path, table_name)

    community_args = []
    table_name = 'myo_community'
    print('-->', client, community_args, db_path, table_name)
    print('--> Executing community_export_sqlite()...')
    print()
    community_export_sqlite(client, community_args, db_path, table_name)

    community_member_role_args = []
    table_name = 'myo_community_member_role'
    print('-->', client, community_member_role_args, db_path, table_name)
    print('--> Executing community_member_role_export_sqlite()...')
    print()
    community_member_role_export_sqlite(client, community_member_role_args, db_path, table_name)

    community_employee_args = []
    table_name = 'myo_community_employee'
    print('-->', client, community_employee_args, db_path, table_name)
    print('--> Executing community_employee_export_sqlite()...')
    print()
    community_employee_export_sqlite(client, community_employee_args, db_path, table_name)

    community_address_args = []
    table_name = 'myo_community_address'
    print('-->', client, community_address_args, db_path, table_name)
    print('--> Executing community_address_export_sqlite()...')
    print()
    community_address_export_sqlite(client, community_address_args, db_path, table_name)

    community_person_args = []
    table_name = 'myo_community_person'
    print('-->', client, community_person_args, db_path, table_name)
    print('--> Executing community_person_export_sqlite()...')
    print()
    community_person_export_sqlite(client, community_person_args, db_path, table_name)

    event_category_args = []
    table_name = 'myo_event_category'
    print('-->', client, event_category_args, db_path, table_name)
    print('--> Executing event_category_export_sqlite()...')
    print()
    event_category_export_sqlite(client, event_category_args, db_path, table_name)

    event_args = []
    table_name = 'myo_event'
    print('-->', client, event_args, db_path, table_name)
    print('--> Executing event_export_sqlite()...')
    print()
    event_export_sqlite(client, event_args, db_path, table_name)

    event_participant_role_args = []
    table_name = 'myo_event_participant_role'
    print('-->', client, event_participant_role_args, db_path, table_name)
    print('--> Executing event_participant_role_export_sqlite()...')
    print()
    event_participant_role_export_sqlite(client, event_participant_role_args, db_path, table_name)

    event_person_args = []
    table_name = 'myo_event_person'
    print('-->', client, event_person_args, db_path, table_name)
    print('--> Executing event_person_export_sqlite()...')
    print()
    event_person_export_sqlite(client, event_person_args, db_path, table_name)

    event_employee_args = []
    table_name = 'myo_event_employee'
    print('-->', client, event_employee_args, db_path, table_name)
    print('--> Executing event_employee_export_sqlite()...')
    print()
    event_employee_export_sqlite(client, event_employee_args, db_path, table_name)

    ir_sequence_args = []
    table_name = 'ir_sequence'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string)
    print('--> Executing ir_sequence_export_sqlite()...')
    print()
    ir_sequence_export_sqlite(client, ir_sequence_args, db_path, table_name, conn_string)


def jcafb_import_sqlite(client, db_path, conn_string):

    res_partner_args = []
    table_name = 'res_partner'
    print('-->', client, res_partner_args, db_path, table_name)
    print('--> Executing res_partner_import_sqlite()...')
    print()
    res_partner_import_sqlite(client, res_partner_args, db_path, table_name)

    res_users_args = []
    table_name = 'res_users'
    print('-->', client, res_users_args, db_path, table_name)
    print('--> Executing res_users_import_sqlite()...')
    print()
    res_users_import_sqlite(client, res_users_args, db_path, table_name)

    hr_department_args = []
    table_name = 'hr_department'
    print('-->', client, hr_department_args, db_path, table_name)
    print('--> Executing hr_department_import_sqlite()...')
    print()
    hr_department_import_sqlite(client, hr_department_args, db_path, table_name)

    hr_employee_args = []
    table_name = 'hr_employee'
    hr_department_table_name = 'hr_department'
    res_partner_table_name = 'res_partner'
    res_users_table_name = 'res_users'
    print(
        '-->',
        client, hr_employee_args, db_path, table_name, hr_department_table_name,
        res_partner_table_name, res_users_table_name
    )
    print('--> Executing hr_employee_import_sqlite()...')
    print()
    hr_employee_import_sqlite(
        client, hr_employee_args, db_path, table_name, hr_department_table_name,
        res_partner_table_name, res_users_table_name
    )

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

    person_category_args = []
    table_name = 'myo_address_category'
    print('-->', client, person_category_args, db_path, table_name)
    print('--> Executing address_category_import_sqlite()...')
    print()
    address_category_import_sqlite(client, person_category_args, db_path, table_name)

    address_args = []
    table_name = 'myo_address'
    tag_table_name = 'myo_tag'
    category_table_name = 'myo_address_category'
    print('-->', client, address_args, db_path, table_name, tag_table_name, category_table_name)
    print('--> Executing address_import_sqlite()...')
    print()
    address_import_sqlite(client, address_args, db_path, table_name, tag_table_name, category_table_name)

    person_category_args = []
    table_name = 'myo_address_category'
    print('-->', client, person_category_args, db_path, table_name)
    print('--> Executing person_category_import_sqlite()...')
    print()
    person_category_import_sqlite(client, person_category_args, db_path, table_name)

    person_args = []
    table_name = 'myo_person'
    tag_table_name = 'myo_tag'
    category_table_name = 'myo_person_category'
    address_table_name = 'myo_address'
    print('-->', client, person_args, db_path, table_name, tag_table_name, category_table_name, address_table_name)
    print('--> Executing person_import_sqlite()...')
    print()
    person_import_sqlite(
        client, person_args, db_path, table_name, tag_table_name, category_table_name, address_table_name
    )

    person_address_role_args = []
    table_name = 'myo_person_address_role'
    print('-->', client, person_address_role_args, db_path, table_name)
    print('--> Executing person_address_role_import_sqlite()...')
    print()
    person_address_role_import_sqlite(client, person_address_role_args, db_path, table_name)

    person_address_args = []
    table_name = 'myo_person_address'
    tag_table_name = 'myo_tag'
    role_table_name = 'myo_person_address_role'
    person_table_name = 'myo_person'
    address_table_name = 'myo_address'
    print(
        '-->', client, person_address_args, db_path, table_name, tag_table_name,
        role_table_name, person_table_name, address_table_name
    )
    print('--> Executing person_address_import_sqlite()...')
    print()
    person_address_import_sqlite(
        client, person_address_args, db_path, table_name, tag_table_name,
        role_table_name, person_table_name, address_table_name
    )

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
    category_table_name = 'myo_person_category'
    address_mng_table_name = 'myo_address_mng'
    address_table_name = 'myo_address'
    person_table_name = 'myo_person'
    print(
        '-->', client, person_mng_args, db_path,
        table_name, tag_table_name, category_table_name,
        address_mng_table_name, address_table_name, person_table_name
    )
    print('--> Executing person_mng_import_sqlite()...')
    print()
    person_mng_import_sqlite(
        client, person_mng_args, db_path,
        table_name, tag_table_name, category_table_name,
        address_mng_table_name, address_table_name, person_table_name
    )

    community_category_args = []
    table_name = 'myo_community_category'
    print('-->', client, community_category_args, db_path, table_name)
    print('--> Executing community_category_import_sqlite()...')
    print()
    community_category_import_sqlite(client, community_category_args, db_path, table_name)

    community_args = []
    table_name = 'myo_community'
    tag_table_name = 'myo_tag'
    category_table_name = 'myo_community_category'
    res_users_table_name = 'res_users'
    print(
        '-->',
        client, community_args, db_path, table_name, tag_table_name, category_table_name, res_users_table_name
    )
    print('--> Executing community_import_sqlite()...')
    print()
    community_import_sqlite(
        client, community_args, db_path, table_name, tag_table_name, category_table_name, res_users_table_name
    )

    community_member_role_args = []
    table_name = 'myo_community_member_role'
    print('-->', client, community_member_role_args, db_path, table_name)
    print('--> Executing community_member_role_import_sqlite()...')
    print()
    community_member_role_import_sqlite(client, community_member_role_args, db_path, table_name)

    community_employee_args = []
    table_name = 'myo_community_employee'
    tag_table_name = 'myo_tag'
    role_table_name = 'myo_community_member_role'
    community_table_name = 'myo_community'
    employee_table_name = 'hr_employee'
    print(
        '-->',
        client, community_employee_args, db_path, table_name, tag_table_name,
        role_table_name, community_table_name, employee_table_name
    )
    print('--> Executing community_employee_import_sqlite()...')
    print()
    community_employee_import_sqlite(
        client, community_employee_args, db_path, table_name, tag_table_name,
        role_table_name, community_table_name, employee_table_name
    )

    community_address_args = []
    table_name = 'myo_community_address'
    tag_table_name = 'myo_tag'
    role_table_name = 'myo_community_member_role'
    community_table_name = 'myo_community'
    address_table_name = 'myo_address'
    print(
        '-->',
        client, community_address_args, db_path, table_name, tag_table_name,
        role_table_name, community_table_name, address_table_name
    )
    print('--> Executing community_address_import_sqlite()...')
    print()
    community_address_import_sqlite(
        client, community_address_args, db_path, table_name, tag_table_name,
        role_table_name, community_table_name, address_table_name
    )

    community_person_args = []
    table_name = 'myo_community_person'
    tag_table_name = 'myo_tag'
    role_table_name = 'myo_community_member_role'
    community_table_name = 'myo_community'
    person_table_name = 'myo_person'
    print(
        '-->',
        client, community_person_args, db_path, table_name, tag_table_name,
        role_table_name, community_table_name, person_table_name
    )
    print('--> Executing community_person_import_sqlite()...')
    print()
    community_person_import_sqlite(
        client, community_person_args, db_path, table_name, tag_table_name,
        role_table_name, community_table_name, person_table_name
    )

    ir_sequence_args = []
    table_name = 'ir_sequence'
    print('-->', client, ir_sequence_args, db_path, table_name, conn_string)
    print('--> Executing ir_sequence_import_sqlite()...')
    print()
    ir_sequence_import_sqlite(client, ir_sequence_args, db_path, table_name, conn_string)


def jcafb_mass_editing_create(client):

    name = 'Address'
    model = 'myo.address'
    fields = ['is_residence', 'state', 'category_ids', 'tag_ids', 'notes', 'active', 'active_log']
    print('-->', client, name, model, fields)
    print('--> Executing mass_editing_create()...')
    mass_editing_create(client, name, model, fields)

    name = 'Person'
    model = 'myo.person'
    fields = ['is_patient', 'state', 'category_ids', 'tag_ids', 'address_id', 'notes', 'active', 'active_log']
    print('-->', client, name, model, fields)
    print('--> Executing mass_editing_create()...')
    mass_editing_create(client, name, model, fields)

    name = 'Person Address'
    model = 'myo.person.address'
    fields = ['address_id', 'role_id', 'sign_in_date', 'sign_out_date', 'tag_ids', 'active', 'active_log']
    print('-->', client, name, model, fields)
    print('--> Executing mass_editing_create()...')
    mass_editing_create(client, name, model, fields)

    name = 'Event'
    model = 'myo.event'
    fields = [
        'user_id', 'state', 'category_ids', 'tag_ids',
        'planned_hours', 'date_start', 'date_foreseen', 'date_deadline',
        'active', 'active_log'
    ]
    print('-->', client, name, model, fields)
    print('--> Executing mass_editing_create()...')
    mass_editing_create(client, name, model, fields)

    name = 'Document'
    model = 'myo.document'
    fields = [
        'user_id', 'state', 'category_ids', 'tag_ids',
        'date_document', 'date_foreseen', 'date_deadline',
        'active', 'active_log'
    ]
    print('-->', client, name, model, fields)
    print('--> Executing mass_editing_create()...')
    mass_editing_create(client, name, model, fields)

    name = 'Survey User Input'
    model = 'survey.user_input'
    fields = [
        'linked_message', 'linked_state',
        'link_survey_user_input', 'active'
    ]
    print('-->', client, name, model, fields)
    print('--> Executing mass_editing_create()...')
    mass_editing_create(client, name, model, fields)

    name = 'Employee'
    model = 'hr.employee'
    fields = [
        'department_id', 'job_id',
        'community_employee_ids', 'event_employee_ids', 'document_employee_ids',
    ]
    print('-->', client, name, model, fields)
    print('--> Executing mass_editing_create()...')
    mass_editing_create(client, name, model, fields)


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


def buffer():
    pass

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

    # ***** 2016-10-07 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-06a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)
    # # myo.tag.code (next = 6)
    # # myo.annotation.code (next = 1)
    # # myo.address.code (next = 153)
    # # myo.document.code (next = 1)
    # # myo.event.code (next = 1)
    # # myo.person.code (next = 208)
    # # myo.community.code (next = 1)
    # # myo.employee.code (next = 17)

    # ***** 2016-10-08 *****
    #

    # person_mng_args = [('state', '=', 'done'), ]
    # batch_name = 'JCAFB_2017_Dados_Fernao_responsible_01'
    # print('-->', client, person_mng_args, batch_name)
    # print('--> Executing person_mng_include_responsible()...')
    # print()
    # person_mng_include_responsible(client, person_mng_args, batch_name)

    # batch_name = 'JCAFB_2017_Dados_Fernao_responsible_01'
    # state = 'waiting'
    # print('-->', client, batch_name, state)
    # print('--> Executing person_mng_create_person()...')
    # person_mng_create_person(client, batch_name, state)

    # person_mng_args = [('state', '=', 'done'), ]
    # print('-->', client, person_mng_args)
    # print('--> Executing person_mng_set_responsible()...')
    # print()
    # person_mng_set_responsible(client, person_mng_args)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-08a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-08a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)
    # # myo.tag.code (next = 7)
    # # myo.annotation.code (next = 1)
    # # myo.address.code (next = 153)
    # # myo.document.code (next = 1)
    # # myo.event.code (next = 1)
    # # myo.person.code (next = 283)
    # # myo.community.code (next = 1)
    # # myo.employee.code (next = 17)

    # ***** 2016-10-11 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-08a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)
    # # myo.tag.code (next = 7)
    # # myo.annotation.code (next = 1)
    # # myo.address.code (next = 153)
    # # myo.document.code (next = 1)
    # # myo.event.code (next = 1)
    # # myo.person.code (next = 283)
    # # myo.community.code (next = 1)
    # # myo.employee.code (next = 17)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-11a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-11a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)
    # # myo.tag.code (next = 7)
    # # myo.annotation.code (next = 1)
    # # myo.address.code (next = 153)
    # # myo.document.code (next = 1)
    # # myo.event.code (next = 1)
    # # myo.person.code (next = 283)
    # # myo.community.code (next = 1)
    # # myo.employee.code (next = 17)

    # ***** 2016-10-21 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-11a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)
    # # myo.tag.code (next = 7)
    # # myo.annotation.code (next = 1)
    # # myo.address.code (next = 153)
    # # myo.document.code (next = 1)
    # # myo.event.code (next = 1)
    # # myo.person.code (next = 283)
    # # myo.community.code (next = 1)
    # # myo.employee.code (next = 17)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # print('-->', client)
    # print('--> Executing jcafb_select_residences()...')
    # jcafb_select_residences(client)

    # print('-->', client)
    # print('--> Executing jcafb_select_persons()...')
    # jcafb_select_persons(client)

    # print('-->', client)
    # print('--> Executing jcafb_select_community_residences()...')
    # jcafb_select_community_residences(client)

    # print('-->', client)
    # print('--> Executing jcafb_select_community_persons()...')
    # jcafb_select_community_persons(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_events()...')
    # jcafb_set_events(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_documents()...')
    # jcafb_set_documents(client)

    # # ***** odoo-mint18
    # #
    # # cd '/opt/openerp'
    # # pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev_2016-10-21a.sql
    # # gzip clvhealth_jcafb_dev_2016-10-21a.sql
    # #
    # db_path = 'data/clvhealth_jcafb_2017_2016-10-21a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)
    # #
    # # ***** clvhealh-jcafb-2017-pro
    # #
    # # /etc/init.d/openerp-server stop
    # #
    # # cd '/opt/openerp'
    # # gzip -d clvhealth_jcafb_dev_2016-10-21a.sql.gz
    # # dropdb -i clvhealth_jcafb_pro
    # # createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_pro
    # # psql -f clvhealth_jcafb_dev_2016-10-21a.sql -d clvhealth_jcafb_pro -U postgres -h localhost -p 5432 -q
    # #
    # # su openerp
    # # cd /opt/openerp/mostlyopen_odoo_addons
    # # git pull
    # # cd /opt/openerp/mostlyopen_odoo_addons_extra
    # # git pull
    # # cd /opt/openerp/mostlyopen_odoo_addons_jcafb
    # # git pull
    # # cd /opt/openerp/mostlyopen_odoo_addons_l10n_br
    # # git pull
    # # exit
    # #
    # # /etc/init.d/openerp-server start

    # ***** 2016-10-26 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-21a.sqlite'
    # print('-->', client, db_path)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path)
    # # myo.tag.code (next = 7)
    # # myo.annotation.code (next = 1)
    # # myo.address.code (next = 153)
    # # myo.document.code (next = 1)
    # # myo.event.code (next = 1)
    # # myo.person.code (next = 283)
    # # myo.community.code (next = 1)
    # # myo.employee.code (next = 17)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # print('-->', client)
    # print('--> Executing jcafb_select_residences()...')
    # jcafb_select_residences(client)

    # print('-->', client)
    # print('--> Executing jcafb_select_persons()...')
    # jcafb_select_persons(client)

    # print('-->', client)
    # print('--> Executing jcafb_select_community_residences()...')
    # jcafb_select_community_residences(client)

    # print('-->', client)
    # print('--> Executing jcafb_select_community_persons()...')
    # jcafb_select_community_persons(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_events()...')
    # jcafb_set_events(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_documents()...')
    # jcafb_set_documents(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_surveys()...')
    # jcafb_set_surveys(client)

    # ***** 2016-10-31 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-21a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)
    # # myo.tag.code (next = 7)
    # # myo.annotation.code (next = 1)
    # # myo.address.code (next = 153)
    # # myo.document.code (next = 1)
    # # myo.event.code (next = 1)
    # # myo.person.code (next = 283)
    # # myo.community.code (next = 1)
    # # mmyo.lab_test.code (next = 1)
    # # myo.employee.code (next = 74)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-31a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-31a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-31b.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # ***** 2016-11-02 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-10-31b.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-02a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-02a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # db_path_1 = 'data/clvhealth_jcafb_2017_2016-10-06a.sqlite'
    # db_path_2 = 'data/clvhealth_jcafb_2017_2016-11-02a.sqlite'
    # person_mng_args = []
    # table_name = 'myo_person_mng'
    # print('-->', client, person_mng_args, db_path_1, db_path_2, table_name)
    # print('--> Executing person_mng_check_sqlite()...')
    # print()
    # person_mng_check_sqlite(client, person_mng_args, db_path_1, db_path_2, table_name)

    # # ***** odoo-mint18
    # #
    # # cd '/opt/openerp'
    # # pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev_2016-11-02b.sql
    # # gzip clvhealth_jcafb_dev_2016-11-02b.sql
    # #
    # db_path = 'data/clvhealth_jcafb_2017_2016-11-02b.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-02b.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # ***** 2016-11-07 *****
    #

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-07a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # batch_name = 'JCAFB_2017_Dados_Fernao'
    # state = 'revised'
    # print('-->', client, batch_name, state)
    # print('--> Executing address_mng_import_from_person_mng()...')
    # address_mng_import_from_person_mng(client, batch_name, state)

    # ***** 2016-11-08 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-07a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-08a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-08a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-08b.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-08b.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # ***** 2016-11-09 *****
    #

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-09a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-09a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # person_mng_args = [('state', '=', 'done'), ]
    # batch_name = 'JCAFB_2017_Dados_Fernao_responsible_02'
    # print('-->', client, person_mng_args, batch_name)
    # print('--> Executing person_mng_include_responsible()...')
    # print()
    # person_mng_include_responsible(client, person_mng_args, batch_name)

    # person_mng_args = [('state', '=', 'done'), ]
    # print('-->', client, person_mng_args)
    # print('--> Executing person_mng_set_responsible()...')
    # print()
    # person_mng_set_responsible(client, person_mng_args)

    # # ***** odoo-mint18
    # #
    # # cd '/opt/openerp'
    # # pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev_2016-11-09b.sql
    # # gzip clvhealth_jcafb_dev_2016-11-09b.sql
    # #
    # db_path = 'data/clvhealth_jcafb_2017_2016-11-09b.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-09b.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # ***** 2016-11-10 *****
    #

    # # ***** odoo-mint18
    # #
    # # cd '/opt/openerp'
    # # pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev_2016-11-10a.sql
    # # gzip clvhealth_jcafb_dev_2016-11-10a.sql
    # #
    # db_path = 'data/clvhealth_jcafb_2017_2016-11-10a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)


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
    conn_string = "dbname='" + dbname + "' user='" + db_user + "' host='" + db_server + \
                  "' password='" + db_password + "'"

    # ***** 2016-11-13 *****
    #

    # ***** odoo-mint18
    #
    # cd '/opt/openerp'
    # dropdb -i clvhealth_jcafb_dev
    # createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_dev
    # psql -f clvhealth_jcafb_dev_2016-11-10a.sql -d clvhealth_jcafb_dev -U postgres -h localhost -p 5432 -q
    #
    # db_path = 'data/clvhealth_jcafb_2017_2016-11-10a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-10a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # ***** 2016-11-15 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_users()...')
    # jcafb_set_users(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-10a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # # ***** odoo-mint18
    # #
    # # cd '/opt/openerp'
    # # pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev_2016-11-15a.sql
    # # gzip clvhealth_jcafb_dev_2016-11-15a.sql
    # #
    # # cd '/opt/openerp'
    # # dropdb -i clvhealth_jcafb_dev
    # # createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_dev
    # # psql -f clvhealth_jcafb_dev_2016-11-15a.sql -d clvhealth_jcafb_dev -U postgres -h localhost -p 5432 -q
    # #
    # db_path = 'data/clvhealth_jcafb_2017_2016-11-15a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-15a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # ***** 2016-11-16 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-15a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # ***** odoo-mint18
    #
    # cd '/opt/openerp'
    # pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev_2016-11-16a.sql
    # gzip clvhealth_jcafb_dev_2016-11-16a.sql
    #
    # cd '/opt/openerp'
    # dropdb -i clvhealth_jcafb_dev
    # createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_dev
    # psql -f clvhealth_jcafb_dev_2016-11-16a.sql -d clvhealth_jcafb_dev -U postgres -h localhost -p 5432 -q
    #
    # db_path = 'data/clvhealth_jcafb_2017_2016-11-16a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # ***** 2016-11-17 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-16a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # print('-->', client)
    # print('--> Executing jcafb_set_hr_department()...')
    # jcafb_set_hr_department(client)

    # print('-->', client)
    # print('--> Executing jcafb_set_communities()...')
    # jcafb_set_communities(client)

    # ***** odoo-mint18
    #
    # cd '/opt/openerp'
    # pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev_2016-11-17a.sql
    # gzip clvhealth_jcafb_dev_2016-11-17a.sql
    #
    # cd '/opt/openerp'
    # dropdb -i clvhealth_jcafb_dev
    # createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_dev
    # psql -f clvhealth_jcafb_dev_2016-11-17a.sql -d clvhealth_jcafb_dev -U postgres -h localhost -p 5432 -q
    #
    # db_path = 'data/clvhealth_jcafb_2017_2016-11-17a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    # ***** 2016-11-18 *****
    #

    # print('-->', client)
    # print('--> Executing jcafb_mass_editing_create()...')
    # jcafb_mass_editing_create(client)

    # db_path = 'data/clvhealth_jcafb_2017_2016-11-17a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_import_sqlite()...')
    # jcafb_import_sqlite(client, db_path, conn_string)

    # # ***** odoo-mint18
    # #
    # # cd '/opt/openerp'
    # # pg_dump clvhealth_jcafb_dev -Fp -U postgres -h localhost -p 5432 > clvhealth_jcafb_dev_2016-11-18a.sql
    # # gzip clvhealth_jcafb_dev_2016-11-18a.sql
    # #
    # # cd '/opt/openerp'
    # # dropdb -i clvhealth_jcafb_dev
    # # createdb -O openerp -E UTF8 -T template0 clvhealth_jcafb_dev
    # # psql -f clvhealth_jcafb_dev_2016-11-18a.sql -d clvhealth_jcafb_dev -U postgres -h localhost -p 5432 -q
    # #
    # db_path = 'data/clvhealth_jcafb_2017_2016-11-18a.sqlite'
    # print('-->', client, db_path, conn_string)
    # print('--> Executing jcafb_export_sqlite()...')
    # jcafb_export_sqlite(client, db_path, conn_string)

    print()
    print('--> setup.py', '- Execution time:', secondsToStr(time() - start))
    print()
