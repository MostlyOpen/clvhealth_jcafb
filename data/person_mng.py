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

import csv
import sqlite3
import re

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


def person_mng_import(client, file_name, batch_name):

    tag_id_ZonaRural = tag_get_id(
        client,
        'Zona Rural',
        'Pessoa residente na Zona Rural.')
    tag_id_ZonaUrbana = tag_get_id(
        client,
        'Zona Urbana',
        'Pessoa residente na Zona Urbana.')
    tag_id_Crianca = tag_get_id(
        client,
        'Criança',
        'Pessoa classificada como Crinça.')
    tag_id_Idoso = tag_get_id(
        client,
        'Idoso',
        'Pessoa classificada como Idoso.')
    tag_id_DadosConferidos = tag_get_id(
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
            if street is not False:
                street = street.replace("Alameda Capitao Cavalcanti", "Alameda Capitão Cavalcanti")
                street = street.replace("Coronel Eduardo de Souza Porto", "Avenida Coronel Eduardo de Souza Pôrto")
                street = street.replace("Antonio Cabette", "Rua Antônio Cabette")
                street = street.replace("Antonio Maria Agostinho Simoes", "Rua Antônio Maria Agostinho Simões")
                street = street.replace("Benedito Soares Fidencio", "Rua Benedito Soares Fidêncio")
                street = street.replace("10 de Novembro", "Rua Dez de Novembro")
                street = street.replace("Fernao Dias Paes Leme", "Rua Fernão Dias Paes Leme")
                street = street.replace("Joao Albino", "Rua Joâo Albino")
                street = street.replace("Joao Alves de Mira", "Rua João Alves de Mira")
                street = street.replace("Joao Pastre", "Rua João Pastre")
                street = street.replace("Jose Bonifacio", "Rua José Bonifácio")
                street = street.replace("Jose Sevilha Filho", "Rua José Sevilha Filho")
                street = street.replace("Salvador Dias de Almeida", "Rua Salvador Dias de Almeida")
                street = street.replace("Sebastiao Andre da Fonseca", "Rua Sebastião André da Fonseca")
                street = street.replace("Sete de Setembro", "Rua Sete de Setembro")
                street = street.replace("Vereador Manoel da Silva Juliao", "Rua Vereador Manoel da Silva Julião")

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
            if district is not False:
                district = district.replace("Água de Peroba", "Água da Peroba")
                district = district.replace("Agua de Peroba", "Água da Peroba")
                district = district.replace("Agua da Peroba", "Água da Peroba")
                district = district.replace("Agua do Arroz", "Água do Arroz")
                district = district.replace("Agua Virada", "Água Virada")
                district = district.replace("Poco de Pedra", "Poço de Pedra")
                district = district.replace("Asfalto Galia", "Asfalto Gália")
                district = district.replace("Asfalto GáLia", "Asfalto Gália")

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


def person_mng_export_sqlite(client, args, db_path, table_name):

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
            tag_ids,
            category_ids,
            name,
            alias,
            code,
            gender,
            marital,
            birthday,
            spouse_name,
            spouse_id,
            father_name,
            father_id,
            mother_name,
            mother_id,
            responsible_name,
            responsible_id,
            identification_id,
            otherid,
            rg,
            cpf,
            country_id_2,
            zip,
            country_id,
            state_id,
            city,
            l10n_br_city_id,
            street,
            number,
            street2,
            district,
            phone,
            mobile,
            fax,
            email,
            state,
            notes,
            batch_name,
            date_inclusion,
            address_mng_id,
            address_id,
            person_id,
            active,
            active_log,
            new_id INTEGER
            );
        '''
    )

    person_mng_model = client.model('myo.person.mng')
    person_mng_browse = person_mng_model.browse(args)

    person_mng_count = 0
    for person_mng_reg in person_mng_browse:
        person_mng_count += 1

        print(person_mng_count, person_mng_reg.id, person_mng_reg.code, person_mng_reg.name.encode("utf-8"))

        alias = None
        if person_mng_reg.alias:
            alias = person_mng_reg.alias

        code = None
        if person_mng_reg.code:
            code = person_mng_reg.code

        marital = None
        if person_mng_reg.marital:
            marital = person_mng_reg.marital

        birthday = None
        if person_mng_reg.birthday:
            birthday = person_mng_reg.birthday

        spouse_name = None
        if person_mng_reg.spouse_name:
            spouse_name = person_mng_reg.spouse_name

        spouse_id = None
        if person_mng_reg.spouse_id:
            spouse_id = person_mng_reg.spouse_id.id

        father_name = None
        if person_mng_reg.father_name:
            father_name = person_mng_reg.father_name

        father_id = None
        if person_mng_reg.father_id:
            father_id = person_mng_reg.father_id.id

        mother_name = None
        if person_mng_reg.mother_name:
            mother_name = person_mng_reg.mother_name

        mother_id = None
        if person_mng_reg.mother_id:
            mother_id = person_mng_reg.mother_id.id

        responsible_name = None
        if person_mng_reg.responsible_name:
            responsible_name = person_mng_reg.responsible_name

        responsible_id = None
        if person_mng_reg.responsible_id:
            responsible_id = person_mng_reg.responsible_id.id

        identification_id = None
        if person_mng_reg.identification_id:
            identification_id = person_mng_reg.identification_id

        otherid = None
        if person_mng_reg.otherid:
            otherid = person_mng_reg.otherid

        rg = None
        if person_mng_reg.rg:
            rg = person_mng_reg.rg

        cpf = None
        if person_mng_reg.cpf:
            cpf = person_mng_reg.cpf

        country_id = None
        if person_mng_reg.country_id:
            country_id = person_mng_reg.country_id.id

        country_id_2 = None
        if person_mng_reg.country_id_2:
            country_id_2 = person_mng_reg.country_id_2.id

        city = None
        if person_mng_reg.city:
            city = person_mng_reg.city

        street = None
        if person_mng_reg.street:
            street = person_mng_reg.street

        number = None
        if person_mng_reg.number:
            number = person_mng_reg.number

        street2 = None
        if person_mng_reg.street2:
            street2 = person_mng_reg.street2

        district = None
        if person_mng_reg.district:
            district = person_mng_reg.district

        phone = None
        if person_mng_reg.phone:
            phone = person_mng_reg.phone

        mobile = None
        if person_mng_reg.mobile:
            mobile = person_mng_reg.mobile

        fax = None
        if person_mng_reg.fax:
            fax = person_mng_reg.fax

        email = None
        if person_mng_reg.email:
            email = person_mng_reg.email

        notes = None
        if person_mng_reg.notes:
            notes = person_mng_reg.notes

        address_mng_id = None
        if person_mng_reg.address_mng_id:
            address_mng_id = person_mng_reg.address_mng_id.id

        address_id = None
        if person_mng_reg.address_id:
            address_id = person_mng_reg.address_id.id

        person_id = None
        if person_mng_reg.person_id:
            person_id = person_mng_reg.person_id.id

        cursor.execute('''
            INSERT INTO ''' + table_name + '''(
                id,
                tag_ids,
                category_ids,
                name,
                alias,
                code,
                gender,
                marital,
                birthday,
                spouse_name,
                spouse_id,
                father_name,
                father_id,
                mother_name,
                mother_id,
                responsible_name,
                responsible_id,
                identification_id,
                otherid,
                rg,
                cpf,
                country_id_2,
                zip,
                country_id,
                state_id,
                city,
                l10n_br_city_id,
                street,
                number,
                street2,
                district,
                phone,
                mobile,
                fax,
                email,
                state,
                notes,
                batch_name,
                date_inclusion,
                address_mng_id,
                address_id,
                person_id,
                active,
                active_log
                )
            VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''', (person_mng_reg.id,
                  str(person_mng_reg.tag_ids.id),
                  str(person_mng_reg.category_ids.id),
                  person_mng_reg.name,
                  alias,
                  code,
                  person_mng_reg.gender,
                  marital,
                  birthday,
                  spouse_name,
                  spouse_id,
                  father_name,
                  father_id,
                  mother_name,
                  mother_id,
                  responsible_name,
                  responsible_id,
                  identification_id,
                  otherid,
                  rg,
                  cpf,
                  country_id_2,
                  person_mng_reg.zip,
                  country_id,
                  person_mng_reg.state_id.id,
                  city,
                  person_mng_reg.l10n_br_city_id.id,
                  street,
                  number,
                  street2,
                  district,
                  phone,
                  mobile,
                  fax,
                  email,
                  person_mng_reg.state,
                  notes,
                  person_mng_reg.batch_name,
                  person_mng_reg.date_inclusion,
                  address_mng_id,
                  address_id,
                  person_id,
                  person_mng_reg.active,
                  person_mng_reg.active_log,
                  )
        )

    conn.commit()
    conn.close()

    print()
    print('--> person_mng_count: ', person_mng_count)


def person_mng_import_sqlite(client, args, db_path, table_name, tag_table_name, category_table_name, address_mng_table_name, address_table_name, person_table_name):

    person_mng_model = client.model('myo.person.mng')

    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor2 = conn.cursor()

    data = cursor.execute(
        '''
        SELECT
            id,
            tag_ids,
            category_ids,
            name,
            alias,
            code,
            gender,
            marital,
            birthday,
            spouse_name,
            spouse_id,
            father_name,
            father_id,
            mother_name,
            mother_id,
            responsible_name,
            responsible_id,
            identification_id,
            otherid,
            rg,
            cpf,
            country_id_2,
            zip,
            country_id,
            state_id,
            city,
            l10n_br_city_id,
            street,
            number,
            street2,
            district,
            phone,
            mobile,
            fax,
            email,
            state,
            notes,
            batch_name,
            date_inclusion,
            address_mng_id,
            address_id,
            person_id,
            active,
            active_log,
            new_id
        FROM ''' + table_name + ''';
        '''
    )

    print(data)
    print([field[0] for field in cursor.description])
    person_mng_count = 0
    for row in cursor:
        person_mng_count += 1

        print(person_mng_count, row['id'], row['name'], row['code'], row['batch_name'])

        values = {
            # 'tag_ids': row['tag_ids'],
            # 'category_ids': row['category_ids'],
            'name': row['name'],
            'alias': row['alias'],
            'code': row['code'],
            'gender': row['gender'],
            'marital': row['marital'],
            'birthday': row['birthday'],
            'spouse_name': row['spouse_name'],
            'spouse_id': row['spouse_id'],
            'father_name': row['father_name'],
            'father_id': row['father_id'],
            'mother_name': row['mother_name'],
            'mother_id': row['mother_id'],
            'responsible_name': row['responsible_name'],
            'responsible_id': row['responsible_id'],
            'identification_id': row['identification_id'],
            'otherid': row['otherid'],
            'rg': row['rg'],
            'cpf': row['cpf'],
            'country_id_2': row['country_id_2'],
            'zip': row['zip'],
            'country_id': row['country_id'],
            'state_id': row['state_id'],
            'city': row['city'],
            'l10n_br_city_id': row['l10n_br_city_id'],
            'street': row['street'],
            'number': row['number'],
            'street2': row['street2'],
            'district': row['district'],
            'phone': row['phone'],
            'mobile': row['mobile'],
            'fax': row['fax'],
            'email': row['email'],
            'state': row['state'],
            'notes': row['state'],
            'batch_name': row['batch_name'],
            'date_inclusion': row['date_inclusion'],
            # 'address_mng_id': row['address_mng_id'],
            # 'address_id': row['address_id'],
            # 'person_id': row['person_id'],
            'active': row['active'],
            'active_log': row['active_log'],
        }
        person_mng_id = person_mng_model.create(values).id

        cursor2.execute(
            '''
           UPDATE ''' + table_name + '''
           SET new_id = ?
           WHERE id = ?;''',
            (person_mng_id,
             row['id']
             )
        )

        if row['tag_ids'] != '[]':

            tag_ids = row['tag_ids'].split(',')
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
                person_mng_model.write(person_mng_id, values)

                new_tag_ids.append(new_tag_id)

            print('>>>>>', row['tag_ids'], new_tag_ids)

        if row['category_ids'] != '[]':

            category_ids = row['category_ids'].split(',')
            new_category_ids = []
            for x in range(0, len(category_ids)):
                category_id = int(re.sub('[^0-9]', '', category_ids[x]))
                cursor2.execute(
                    '''
                    SELECT new_id
                    FROM ''' + category_table_name + '''
                    WHERE id = ?;''',
                    (category_id,
                     )
                )
                new_category_id = cursor2.fetchone()[0]

                values = {
                    'category_ids': [(4, new_category_id)],
                }
                person_mng_model.write(person_id, values)

                new_category_ids.append(new_category_id)

            print('>>>>>', row['category_ids'], new_category_ids)

        if row['address_mng_id']:

            address_mng_id = row['address_mng_id']

            cursor2.execute(
                '''
                SELECT new_id
                FROM ''' + address_mng_table_name + '''
                WHERE id = ?;''',
                (address_mng_id,
                 )
            )
            new_address_mng_id = cursor2.fetchone()[0]

            values = {
                'address_mng_id': new_address_mng_id,
            }
            person_mng_model.write(person_mng_id, values)

            print('>>>>>', row['address_mng_id'], new_address_mng_id)

        if row['address_id']:

            address_id = row['address_id']

            cursor2.execute(
                '''
                SELECT new_id
                FROM ''' + address_table_name + '''
                WHERE id = ?;''',
                (address_id,
                 )
            )
            new_address_id = cursor2.fetchone()[0]

            values = {
                'address_id': new_address_id,
            }
            person_mng_model.write(person_mng_id, values)

            print('>>>>>', row['address_id'], new_address_id)

        if row['person_id']:

            person_id = row['person_id']

            cursor2.execute(
                '''
                SELECT new_id
                FROM ''' + person_table_name + '''
                WHERE id = ?;''',
                (person_id,
                 )
            )
            new_person_id = cursor2.fetchone()[0]

            values = {
                'person_id': new_person_id,
            }
            person_mng_model.write(person_mng_id, values)

            print('>>>>>', row['person_id'], new_person_id)

    conn.commit()
    conn.close()

    print()
    print('--> person_mng_count: ', person_mng_count)


def person_mng_include_responsible(client, args, batch_name):

    tag_id_VerificarCadastro = tag_get_id(
        client,
        'Verificar Cadastro',
        'Os dados de cadastro do registro precisam ser verificados.')

    tag_ids = []
    tag_ids = tag_ids + [(4, tag_id_VerificarCadastro)]

    person_mng_model = client.model('myo.person.mng')

    person_mng_browse = person_mng_model.browse(
        args +
        [('responsible_name', '!=', False), ]
    )

    responsible_count = 0
    new_person_mng_count = 0
    for person_mng_reg in person_mng_browse:
        responsible_count += 1
        print(responsible_count, person_mng_reg.responsible_name)

        person_mng_browse_2 = person_mng_model.browse([('name', '=', person_mng_reg.responsible_name), ])
        if person_mng_browse_2.id == []:
            new_person_mng_count += 1

            values = {
                'name': person_mng_reg.responsible_name,
                'code': False,
                'address_id': person_mng_reg.address_id.id,
                'address_mng_id': person_mng_reg.address_mng_id.id,
                'batch_name': batch_name,
                'state': 'waiting',
                'tag_ids': tag_ids,
                'zip': person_mng_reg.zip,
                'country_id': person_mng_reg.country_id.id,
                'state_id': person_mng_reg.state_id.id,
                'l10n_br_city_id': person_mng_reg.l10n_br_city_id.id,
                'street': person_mng_reg.street,
                'number': person_mng_reg.number,
                'street2': person_mng_reg.street2,
                'district': person_mng_reg.district,
                'phone': person_mng_reg.phone,
                'mobile': person_mng_reg.mobile,
            }
            person_mng_new = person_mng_model.create(values)
            print('>>>>>', person_mng_new)

    print()
    print('--> responsible_count: ', responsible_count)
    print('--> new_person_mng_count: ', new_person_mng_count)
    print()


def person_mng_set_responsible(client, args):

    person_mng_model = client.model('myo.person.mng')
    person_model = client.model('myo.person')

    person_mng_browse = person_mng_model.browse(
        args +
        [('responsible_name', '!=', False),
         ('responsible_id', '=', False),
         ]
    )

    responsible_count = 0
    for person_mng_reg in person_mng_browse:
        responsible_count += 1
        print(responsible_count, person_mng_reg.responsible_name)

        person_browse = person_model.browse([('name', '=', person_mng_reg.responsible_name), ])
        if person_browse.id != []:
            responsible_id = person_browse.id[0]
            print('>>>>>', responsible_id)

            values = {
                "responsible_id": responsible_id,
            }
            person_mng_model.write(person_mng_reg.id, values)

            values = {
                "responsible_id": responsible_id,
            }
            person_model.write(person_mng_reg.person_id.id, values)

    print()
    print('--> responsible_count: ', responsible_count)
    print()
