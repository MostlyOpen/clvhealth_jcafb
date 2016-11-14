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

import xlrd

# from odoo_api import *

# from address_mng import *
# from person_mng import *
# from jcafb_2017_users import *
# from jcafb_2017_communities import *
# from jcafb_2017_residences import *
# from jcafb_2017_persons import *
# from jcafb_2017_events import *
# from jcafb_2017_documents import *
# from jcafb_2017_surveys import *


def ir_model_data_get_instance(client, code):

    code = code.replace('[', '')
    code = code.replace(']', '')
    ir_model_data = client.model('ir.model.data')
    ir_model_data_browse = ir_model_data.browse([('name', '=', code), ])

    if ir_model_data_browse.name != []:
        instance = ir_model_data_browse.name[0], ir_model_data_browse.model[0], ir_model_data_browse.res_id[0]
        return instance
    else:
        instance = False, False, False
        return instance


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
    print('--> excel.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)
    conn_string = "dbname='" + dbname + "' user='" + db_user + "' host='" + db_server + \
                  "' password='" + db_password + "'"

    book = xlrd.open_workbook('data/survey_jcafb_QAN17.xls')

    survey_question = client.model('survey.question')
    survey_label = client.model('survey.label')

    # for sheet in book.sheets():
    #     print(sheet.name)

    # sheet = book.sheet_by_name('QAN17')
    sheet = book.sheet_by_index(0)
    print(sheet.name)
    # print(dir(sheet))
    print(sheet.nrows)
    print(sheet.ncols)

    survey_title = sheet.cell_value(0, 0)
    print('>>>>>', '"' + survey_title + '"')

    survey_model = client.model('survey.survey')
    survey_browse = survey_model.browse([('title', '=', survey_title), ])
    print('>>>>>', survey_browse)
    title_ok = False

    if survey_browse.id != []:
        title = survey_browse[0].title
        description = survey_browse[0].description
        print('>>>>>', title, description)
        if title == survey_title:
            title_ok = True

    print('>>>>> title_ok: ', title_ok)

    for i in range(sheet.nrows):

        row = sheet.row_values(i)
        code_row = sheet.cell_value(i, 0)

        if code_row == '[]':
            code_cols = {}
            for k in range(sheet.ncols):
                code_col = sheet.cell_value(i, k)
                if code_col != xlrd.empty_cell.value:
                    code_cols.update({k: code_col})

        for j in range(sheet.ncols):

            if sheet.cell_value(i, j) != xlrd.empty_cell.value:

                if sheet.cell_value(i, j) == 'free_text':
                    question_type = 'free_text'
                if sheet.cell_value(i, j) == 'textbox':
                    question_type = 'textbox'
                if sheet.cell_value(i, j) == 'datetime':
                    question_type = 'datetime'
                if sheet.cell_value(i, j) == 'simple_choice':
                    question_type = 'simple_choice'
                if sheet.cell_value(i, j) == 'multiple_choice':
                    question_type = 'multiple_choice'
                if sheet.cell_value(i, j) == 'matrix_simple':
                    question_type = 'matrix_simple'

                if sheet.cell_value(i, j) == '.':
                    try:
                        value = sheet.cell_value(i, j + 1)
                    except:
                        value = xlrd.empty_cell.value
                    if value != xlrd.empty_cell.value:
                        print()
                        print('>>>>> (', i, j + 1, ')', value)

                        if question_type == 'textbox':
                            # print('>>>>>>>>>>', code_row)
                            instance_row = ir_model_data_get_instance(client, code_row)
                            # print('------>', instance_row)
                            if instance_row[1] == 'survey.question':
                                survey_question_browse = survey_question.browse([
                                    ('id', '=', instance_row[2]),
                                ])

                                print('------>(textbox)', survey_question_browse[0].question.encode('utf-8'))

                        if question_type == 'simple_choice':
                            # print('>>>>>>>>>>', code_row)
                            instance_row = ir_model_data_get_instance(client, code_row)
                            # print('------>', instance_row)
                            if instance_row[1] == 'survey.question':
                                survey_question_browse = survey_question.browse([
                                    ('id', '=', instance_row[2]),
                                ])

                                print(
                                    '------>(simple_choice_question)',
                                    survey_question_browse[0].question.encode('utf-8')
                                )
                                print(
                                    '------>(simple_choice_comment)',
                                    survey_question_browse[0].comments_message.encode('utf-8')
                                )
                            if instance_row[1] == 'survey.label':
                                survey_label_browse = survey_label.browse([
                                    ('id', '=', instance_row[2]),
                                ])

                                print(
                                    '------>(simple_choice_question)',
                                    survey_label_browse[0].question_id.question.encode('utf-8')
                                )
                                print(
                                    '------>(simple_choice_answer)',
                                    survey_label_browse[0].value.encode('utf-8')
                                )

                        if question_type == 'multiple_choice':
                            # print('>>>>>>>>>>', code_row)
                            instance_row = ir_model_data_get_instance(client, code_row)
                            # print('------>', instance_row)
                            if instance_row[1] == 'survey.question':
                                survey_question_browse = survey_question.browse([
                                    ('id', '=', instance_row[2]),
                                ])

                                print(
                                    '------>((multiple_choice_question)',
                                    survey_question_browse[0].question.encode('utf-8')
                                )
                                print(
                                    '------>((multiple_choice_comment)',
                                    survey_question_browse[0].comments_message.encode('utf-8')
                                )
                            if instance_row[1] == 'survey.label':
                                survey_label_browse = survey_label.browse([
                                    ('id', '=', instance_row[2]),
                                ])

                                print(
                                    '------>(simple_choice_question)',
                                    survey_label_browse[0].question_id.question.encode('utf-8')
                                )
                                print(
                                    '------>(simple_choice_answer)',
                                    survey_label_browse[0].value.encode('utf-8')
                                )

                        if question_type == 'matrix_simple':
                            code_col = code_cols[j]
                            # print('>>>>>>>>>>', code_row, code_col)
                            instance_row = ir_model_data_get_instance(client, code_row)
                            # print('------>', instance_row)
                            instance_col = ir_model_data_get_instance(client, code_col)
                            # print('------>', instance_col)
                            if instance_row[1] == 'survey.label':
                                survey_label_browse = survey_label.browse([
                                    ('id', '=', instance_row[2]),
                                ])

                                print(
                                    '------>(matrix_simple_row)',
                                    survey_label_browse[0].value.encode('utf-8')
                                )
                            if instance_col[1] == 'survey.label':
                                survey_label_browse = survey_label.browse([
                                    ('id', '=', instance_col[2]),
                                ])

                                print(
                                    '------>(matrix_simple_col)',
                                    survey_label_browse[0].value.encode('utf-8')
                                )

    print()
    print('--> excel.py', '- Execution time:', secondsToStr(time() - start))
    print()
