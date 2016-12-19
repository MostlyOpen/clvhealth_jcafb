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

import base

import xmlrpclib


def user_groups_set_myo_address(user_name):

    print 'Executing user_groups_set_myo_address...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_address
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Address User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Address Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Address Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_address_mng(user_name):

    print 'Executing user_groups_set_myo_address_mng...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_address_mng
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Address Management User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Address Management Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_annotation(user_name):

    print 'Executing user_groups_set_myo_annotation...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_annotation
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Annotation User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Annotation Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Annotation Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_base(user_name):

    '''
    Reference: http://help.openerp.com/question/18704/hide-menu-for-existing-group/

    There are actually0-6 numbers for representing each job for a many2many/ one2many field

        (0, 0, { values }) -- link to a new record that needs to be created with the given values dictionary
        (1, ID, { values }) -- update the linked record with id = ID (write values on it)
        (2, ID) -- remove and delete the linked record with id = ID (calls unlink on ID, that will delete the
                   object completely, and the link to it as well)
        (3, ID) -- cut the link to the linked record with id = ID (delete the relationship between the two
                   objects but does not delete the target object itself)
        (4, ID) -- link to existing record with id = ID (adds a relationship)
        (5) -- unlink all (like using (3,ID) for all linked records)
        (6, 0, [IDs]) -- replace the list of linked IDs (like using (5) then (4,ID) for each ID in the list of IDs)
    '''

    print 'Executing user_groups_set_myo_base...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_base
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'User (myo)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Super User (myo)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Manager (myo)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Register Manager (myo)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Super Manager (myo)')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_community(user_name):

    print 'Executing user_groups_set_myo_community...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_community
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Community User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Community Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_document(user_name):

    print 'Executing user_groups_set_myo_document...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_document
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Document User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Document Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Document Approver')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Document Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_event(user_name):

    print 'Executing user_groups_set_myo_event...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_event
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Event User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Event Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Event Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_lab_test(user_name):

    print 'Executing user_groups_set_myo_lab_test...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_lab_test
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Lab Test User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Lab Test Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Lab Test Approver')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_patient(user_name):

    print 'Executing user_groups_set_myo_patient...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_patient
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Patient User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Patient Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_person(user_name):

    print 'Executing user_groups_set_myo_person...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_person
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_person_mng(user_name):

    print 'Executing user_groups_set_myo_person_mng...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_person_mng
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person Management User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Person Management Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_professional(user_name):

    print 'Executing user_groups_set_myo_professional...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_professional
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Professional User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Professional Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Professional Category Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Professional Specialty Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_residence(user_name):

    print 'Executing user_groups_set_myo_residence...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_residence
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Residence User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Residence Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_summary(user_name):

    print 'Executing user_groups_set_myo_summary...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_summary
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Summary User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Summary Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'


def user_groups_set_myo_tag(user_name):

    print 'Executing user_groups_set_myo_tag...'

    sock_common = xmlrpclib.ServerProxy(base.sock_common_url)
    uid = sock_common.login(base.dbname, base.admin_user, base.admin_user_pw)
    sock = xmlrpclib.ServerProxy(base.sock_str)

    args = [('name', '=', user_name), ]
    user_id = sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'search', args)

    # myo_tag
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Tag User')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)
    values = {
        'groups_id': [(
            4, sock.execute(base.dbname, uid, base.admin_user_pw,
                            'res.groups', 'search', [('name', '=', 'Tag Manager')]
                            )[0]
        )],
    }
    sock.execute(base.dbname, uid, base.admin_user_pw, 'res.users', 'write', user_id, values)

    print 'Done.'
