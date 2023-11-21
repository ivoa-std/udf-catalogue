# -*- format: utf-8 -*-

# Pools the registry for ADQL User Defined Functions (UDF) and
# subsequently creates a restructuredText file which cointaints a
# signature and description, per each unique UDF encountered

import requests
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

HTTP_TIMEOUT = 5

# we must have timeouts on our requests; there should be a way to do
# that in pyVO, but for now there is not.

class SessionWithTimeout(requests.Session):
    def request(self, *args, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = HTTP_TIMEOUT
        return super().request(*args, **kwargs)

requests.Session = SessionWithTimeout


def get_udfs_for_service(service):
    """yields (form, description) pairs for the UDFs of a TAPService.
    """
    for capability in service.capabilities:
        if ('TAP' in capability.standardid
                and isinstance(capability, TableAccess)):
            for language in capability.languages:
                for langfeatlist in language.languagefeaturelists:
                    for feature in langfeatlist:
                        yield {
                            NAME_FIELD: feature.form,
                            DESC_FIELD: feature.description}


def main():
    udf_list = []
    for service_record in regsearch(servicetype='tap'):
        print("Querying service {}...".format(service_record.short_name))
        try:
            udf_list.extend(get_udfs_for_service(
                service_record.get_service("tap")))

        except KeyboardInterrupt:
            print("   ...skipped")
            # let users ^C out if they want
            time.sleep(0.5)

        except Exception as exc:
            print(f"    ...failed ({exc})")

    udf_list = sorted(
        {v[NAME_FIELD]:v for v in udf_list}.values(),
        key=lambda v: v[NAME_FIELD])

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


if __name__=="__main__":
    main()
