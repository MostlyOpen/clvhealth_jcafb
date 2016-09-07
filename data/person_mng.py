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
import csv

from odoo_api import *


def str_title(string):

    string = string.strip()
    string = string.replace("  ", " ")
    string = string.replace("  ", " ")
    string = string.title()
    string = string.replace(" Da ", " da ")
    string = string.replace(" De ", " de ")
    string = string.replace(" Di ", " di ")
    string = string.replace(" Do ", " do ")
    string = string.replace(" Dos ", " dos ")
    string = string.replace(" E ", " e ")
    string = string.replace("ÁC", "ác")
    string = string.replace("ÂN", "ân")
    string = string.replace("ÃO", "ão")
    string = string.replace("ÁT", "át")
    string = string.replace("ÇA", "ça")
    string = string.replace("ÇÃO", "ção")
    string = string.replace("ÇO", "ço")
    string = string.replace("D'ÁG", "D'Ág")
    string = string.replace("ÉL", "él")
    string = string.replace("ÊN", "ên")
    string = string.replace("ÉU", "éu")
    string = string.replace("ÍC", "íc")
    string = string.replace("ÍN", "ín")
    string = string.replace("ÍR", "Ír")
    string = string.replace("ÍT", "ít")
    string = string.replace("ÔN", "ôn")
    string = string.replace("ÔR", "ôr")
    string = string.replace("ÓR", "ór")
    string = string.replace("ÚJ", "új")
    string = string.replace("ÚN", "ún")
    string = string.replace("Á", "á")
    string = string.replace("É", "é")
    string = string.replace("D'á", "D'Á")
    string = string.replace("áGua", "Água")

    return string


def person_mng_model_import(client, file_name, batch_name):

    tag_id_ZonaRural = myo_tag_get_id(
        client,
        'Zona Rural',
        'Pessoa residente na Zona Rural.')
    tag_id_ZonaUrbana = myo_tag_get_id(
        client,
        'Zona Urbana',
        'Pessoa residente na Zona Urbana.')
    tag_id_Crianca = myo_tag_get_id(
        client,
        'Criança',
        'Pessoa classificada como Crinça.')
    tag_id_Idoso = myo_tag_get_id(
        client,
        'Idoso',
        'Pessoa classificada como Idoso.')
    tag_id_DadosConferidos = myo_tag_get_id(
        client,
        'Dados Conferidos',
        'Os dados do registro já foram conferidos.')

    delimiter_char = ';'

    file = open(file_name, "rb")
    reader = csv.reader(file, delimiter=delimiter_char)
    rownum = 0
    imported = 0
    not_imported = 0
    column_name = {}
    for row in reader:

        rowlen = len(row)

        if rownum == 0:

            column_num = 0
            for column in row:
                column_name[column] = column_num
                column_num += 1

            print(rownum, row, rowlen)

            rownum += 1
            continue

        person_mng_model = client.model('myo.person.mng')

        if len(row) == rowlen:
            print(rownum,
                  row[column_name['Nome completo']].decode('utf-8'),
                  row[column_name['Tipo']].decode('utf-8'),
                  row, rowlen)

            name = str_title(row[column_name['Nome completo']])

            gender = row[column_name['Sexo']]

            notes = ''
            notes = notes + 'Idade: ' + row[column_name['Idade']] + '\n'

            birthday = row[column_name['Data de nasc.']]
            if birthday == '' or birthday == '-':
                birthday = False
            if birthday == '2016/12/06':
                notes = notes + 'Data de Nasc.: ' + row[column_name['Data de nasc.']] + '\n'
                birthday = False
            if birthday is not False:
                if birthday[2] == '/':
                    birthday = birthday.replace("/", "")
                    d = [0, 2, 4, 8]
                    dd = [birthday[d[j - 1]:d[j]] for j in range(1, len(d))]
                    birthday = '%s-%s-%s' % (dd[2], dd[1], dd[1])
                if birthday[4] == '/':
                    birthday = birthday.replace("/", "-")

            tag_ids = []
            if row[column_name['Zona']] == 'URBANA':
                tag_ids = tag_ids + [(4, tag_id_ZonaUrbana)]
            if row[column_name['Zona']] == 'RURAL':
                tag_ids = tag_ids + [(4, tag_id_ZonaRural)]
            if row[column_name['Tipo']] == 'CRIANÇA':
                tag_ids = tag_ids + [(4, tag_id_Crianca)]
            if row[column_name['Tipo']] == 'IDOSO':
                tag_ids = tag_ids + [(4, tag_id_Idoso)]
            if row[column_name['Dados conferidos?']] == 'SIM':
                tag_ids = tag_ids + [(4, tag_id_DadosConferidos)]

            cep = '17455-000'
            l10n_br_zip = client.model('l10n_br.zip')
            l10n_br_zip_browse = l10n_br_zip.browse([('zip', '=', re.sub('[^0-9]', '', cep)), ])
            zip_id = l10n_br_zip_browse.id
            if zip_id != []:
                zip_ = l10n_br_zip_browse[0].zip
                val = re.sub('[^0-9]', '', zip_)
                if len(val) == 8:
                    zip_ = "%s-%s" % (val[0:5], val[5:8])
                country_id = l10n_br_zip_browse[0].country_id.id
                state_id = l10n_br_zip_browse[0].state_id.id
                l10n_br_city_id = l10n_br_zip_browse[0].l10n_br_city_id.id

            street = str_title(row[column_name['Endereço']])
            if street == '' or street == '-':
                street = False

            number = row[column_name['Número']]
            number = number.strip()
            number = number.replace("  ", " ")
            number = number.replace("  ", " ")
            if number == 'S/N':
                number = False
            if number == '':
                number = False

            street2 = str_title(row[column_name['Complemento']])
            if street2 == '':
                street2 = False

            district = str_title(row[column_name['Bairro']])
            if district == '' or district == '-':
                district = False
            if district == 'Água de Peroba':
                district = 'Água da Peroba'
            if district == 'Agua da Peroba':
                district = 'Água da Peroba'
            if district == 'Agua do Arroz':
                district = 'Água do Arroz'
            if district == 'Agua Virada':
                district = 'Água Virada'
            if district == 'Poco de Pedra':
                district = 'Poço de Pedra'

            phone = row[column_name['Telefone']]
            if phone == '-':
                phone = False

            responsible_name = str_title(row[column_name['Nome do responsável']])
            if responsible_name == '' or responsible_name == '-':
                responsible_name = False

            notes = notes + 'Dados conferidos?: ' + row[column_name['Dados conferidos?']] + '\n'

            notes = notes + 'Observações: ' + row[column_name['Observações']] + '\n'

            print('>>>>>', name)
            state = 'draft'
            if name is False or name == '':
                state = 'canceled'

            values = {
                'name': name,
                'code': False,
                'batch_name': batch_name,
                'gender': gender,
                'birthday': birthday,
                'tag_ids': tag_ids,
                'zip': zip_,
                'country_id': country_id,
                'state_id': state_id,
                'l10n_br_city_id': l10n_br_city_id,
                'street': street,
                'number': number,
                'street2': street2,
                'district': district,
                'phone': phone,
                'responsible_name': responsible_name,
                'notes': notes,
                'state': state,
            }
            person_mng_model.create(values)

            imported += 1
        else:
            print(rownum, '"Error! len(row) != rowlen"', rowlen, len(row), row)
            not_imported += 1

        rownum += 1

    file.close()

    print()
    print('--> rownum: ', rownum - 1)
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
    print('--> person_mng_model.py...')
    print('--> server:', server)

    get_arguments()

    from time import time
    start = time()

    client = erppeek.Client(server, dbname, username, password)

    print()
    print('--> person_mng_model.py', '- Execution time:', secondsToStr(time() - start))
    print()
