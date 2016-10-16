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
    print('--> Executing jcafb_2017_surveys.py ...')

    yaml_filename = 'FSE17/survey_jcafb_FSE17.yaml'
    yaml_out_filename = 'FSE17/survey_jcafb_FSE17_out.yaml'
    xml_filename = 'FSE17/survey_jcafb_FSE17.xml'
    txt_filename = 'FSE17/survey_jcafb_FSE17.txt'
    print('--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename))
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'ISE17/survey_jcafb_ISE17.yaml'
    yaml_out_filename = 'ISE17/survey_jcafb_ISE17_out.yaml'
    xml_filename = 'ISE17/survey_jcafb_ISE17.xml'
    txt_filename = 'ISE17/survey_jcafb_ISE17.txt'
    print('--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename))
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'CSE17/survey_jcafb_CSE17.yaml'
    yaml_out_filename = 'CSE17/survey_jcafb_CSE17_out.yaml'
    xml_filename = 'CSE17/survey_jcafb_CSE17.xml'
    txt_filename = 'CSE17/survey_jcafb_CSE17.txt'
    print('--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename))
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'QMD17/survey_jcafb_QMD17.yaml'
    yaml_out_filename = 'QMD17/survey_jcafb_QMD17_out.yaml'
    xml_filename = 'QMD17/survey_jcafb_QMD17.xml'
    txt_filename = 'QMD17/survey_jcafb_QMD17.txt'
    print('--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename))
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'LMD17/survey_jcafb_LMD17.yaml'
    yaml_out_filename = 'LMD17/survey_jcafb_LMD17_out.yaml'
    xml_filename = 'LMD17/survey_jcafb_LMD17.xml'
    txt_filename = 'LMD17/survey_jcafb_LMD17.txt'
    print('--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename))
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'QAN17/survey_jcafb_QAN17.yaml'
    yaml_out_filename = 'QAN17/survey_jcafb_QAN17_out.yaml'
    xml_filename = 'QAN17/survey_jcafb_QAN17.xml'
    txt_filename = 'QAN17/survey_jcafb_QAN17.txt'
    print('--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename))
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'QDH17/survey_jcafb_QDH17.yaml'
    yaml_out_filename = 'QDH17/survey_jcafb_QDH17_out.yaml'
    xml_filename = 'QDH17/survey_jcafb_QDH17.xml'
    txt_filename = 'QDH17/survey_jcafb_QDH17.txt'
    print('--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename))
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    yaml_filename = 'ITM17/survey_jcafb_ITM17.yaml'
    yaml_out_filename = 'ITM17/survey_jcafb_ITM17_out.yaml'
    xml_filename = 'ITM17/survey_jcafb_ITM17.xml'
    txt_filename = 'ITM17/survey_jcafb_ITM17.txt'
    print('--> Executing survey_process_yaml(%s, %s, %s) ...' % (yaml_filename, xml_filename, txt_filename))
    survey_process_yaml(yaml_filename, yaml_out_filename, xml_filename, txt_filename)
    if copy_xml_file:
        shutil.copy(xml_filename, destination_directory)

    print('--> jcafb_2017_surveys.py')
    print('--> Execution time:', secondsToStr(time() - start))
