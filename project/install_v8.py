#!/usr/bin/env python
# -*- coding: utf-8 -*-
###############################################################################
#
# Copyright (C) 2016-Today  Carlos Eduardo Vercelino - CLVsol
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
import user_groups_set

import erppeek


def install_update_module(module, update, config_admin=False):

    modules_to_update = base.modules_to_update

    print '%s%s' % ('--> ', module)
    if module in modules_to_update:
        new_module = base.install_update_module(module, True)
    else:
        new_module = base.install_update_module(module, update)

    method = '%s%s' % ('user_groups_set_', module)
    methodToCall = getattr(user_groups_set, method)

    if new_module and config_admin:
        user_name = 'Administrator'
        print '%s%s(%s)' % ('--> ', method, user_name)
        methodToCall(user_name)

        user_name = 'Data Administrator'
        print '%s%s(%s)' % ('--> ', method, user_name)
        methodToCall(user_name)

    return new_module


def clvhealth_jcafb_install():

    update = base.update

    print '--> create_database()'
    newDB = base.create_database()
    if newDB:
        print '--> YourCompany()'
        base.YourCompany()
        print '--> Administrator()'
        base.Administrator()
        print '--> Administrator_groups_id_updt()'
        base.Administrator_groups_id_updt()
        print '--> Demo_User()'
        base.Demo_User()
        print '--> Data_Administrator_User()'
        base.Data_Administrator_User()
    else:
        client = erppeek.Client(base.server,
                                db=base.dbname,
                                user=base.admin_user,
                                password=base.admin_user_pw,
                                verbose=False)
        proxy = client.model('ir.module.module')
        proxy.update_list()

    install_update_module('myo_base', update, True)


def secondsToStr(t):

    return "%d:%02d:%02d.%03d" % \
        reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000,), 1000, 60, 60])


if __name__ == '__main__':

    from time import time

    base.get_arguments()

    start = time()

    print '--> Executing clvhealth_jcafb_install.py...'

    print '--> Executing clvhealth_jcafb_install()...'
    clvhealth_jcafb_install()

    print '--> clvhealth_jcafb_install.py'
    print '--> Execution time:', secondsToStr(time() - start)
