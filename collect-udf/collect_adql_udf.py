# -*- format: utf-8 -*-

# Pools the registry for ADQL User Defined Functions (UDF) and
# subsequently creates a restructuredText file which cointaints a
# signature and description, per each unique UDF encountered

from datetime import datetime
from xml.etree import ElementTree
from itertools import chain
from pyvo.registry import search as regsearch
from pyvo.dal import TAPService
from pyvo.io.vosi.tapregext import TableAccess

NAME_FIELD = "name"
DESC_FIELD = "description"

FILE_NAME = "udf_list.rst"
FILE_TITLE = 'List of third party User Defined functions'

udf_list = []

for service_record in regsearch(servicetype='tap'):
    print("Querying service {}...".format(service_record.short_name))
    service = TAPService(service_record.access_url)
    try:
        for capability in service.capabilities:
            if 'TAP' in capability.standardid and isinstance(capability,
                    TableAccess):
                for language in capability.languages:
                    for langfeatlist in language.languagefeaturelists:
                        for feature in langfeatlist:
                            udf_list.append({
                                NAME_FIELD: feature.form,
                                DESC_FIELD: feature.description})
    except:
        pass

udf_list = list({v[NAME_FIELD]:v for v in udf_list}.values())

with open(FILE_NAME, 'w') as output_file:
    output_file.write(FILE_TITLE + "\n")
    output_file.write("*" * len(FILE_TITLE) + '\n\n')
    output_file.write("Generated with ``collect_adql_udf.py``\n\n")
    output_file.write("Last generated: " +
                      datetime.now().strftime("%Y-%m-%d %H:%M:%S") +
                      "\n\n")
    for udf_item in udf_list:
        udf_name = udf_item[NAME_FIELD]
        udf_desc = udf_item[DESC_FIELD]
        if "(" in udf_name and "ivo_" not in udf_name:
            output_file.write("``" + udf_name + "``" + '\n')
            output_file.write("^" * (len(udf_name) + 4) + "\n")
            if udf_desc is not None:
                output_file.write(udf_desc + "\n")
            output_file.write("\n")
