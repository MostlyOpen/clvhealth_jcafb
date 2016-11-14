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

import shutil


def secondsToStr(t):
    return "%d:%02d:%02d.%03d" % reduce(lambda ll, b: divmod(ll[0], b) + ll[1:], [(t * 1000, ), 1000, 60, 60])


if __name__ == '__main__':

    from time import time
    start = time()

    destination_directory = '/opt/openerp/mostlyopen_odoo_addons_jcafb/jcafb_2017_consent_forms/data'
    copy_xml_file = True

    print('--> Executing jcafb_2017_consent_forms.py ...')

    yaml_filename = 'TCP17/survey_jcafb_TCP17.yaml'
    yaml_out_filename = 'TCP17/survey_jcafb_TCP17_out.yaml'
    xml_filename = 'TCP17/survey_jcafb_TCP17.xml'
    txt_filename = 'TCP17/survey_jcafb_TCP17.txt'
    xls_filename = 'TCP17/survey_jcafb_TCP17.xls'
    print(
        '--> Executing survey_process_yaml(%s, %s, %s, %s) ...' %
        (yaml_filename, xml_filename, txt_filename, xls_filename)
    )
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename, xls_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'TCR17/survey_jcafb_TCR17.yaml'
    yaml_out_filename = 'TCR17/survey_jcafb_TCR17_out.yaml'
    xml_filename = 'TCR17/survey_jcafb_TCR17.xml'
    txt_filename = 'TCR17/survey_jcafb_TCR17.txt'
    xls_filename = 'TCR17/survey_jcafb_TCR17.xls'
    print(
        '--> Executing survey_process_yaml(%s, %s, %s, %s) ...' %
        (yaml_filename, xml_filename, txt_filename, xls_filename)
    )
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename, xls_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'TID17/survey_jcafb_TID17.yaml'
    yaml_out_filename = 'TID17/survey_jcafb_TID17_out.yaml'
    xml_filename = 'TID17/survey_jcafb_TID17.xml'
    txt_filename = 'TID17/survey_jcafb_TID17.txt'
    xls_filename = 'TID17/survey_jcafb_TID17.xls'
    print(
        '--> Executing survey_process_yaml(%s, %s, %s, %s) ...' %
        (yaml_filename, xml_filename, txt_filename, xls_filename)
    )
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename, xls_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    print('--> jcafb_2017_consent_forms.py')
    print('--> Execution time:', secondsToStr(time() - start))
