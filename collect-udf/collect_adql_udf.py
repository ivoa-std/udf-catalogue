# -*- format: utf-8 -*-

# Pools the registry for ADQL User Defined Functions (UDF) and
# subsequently creates a restructuredText file which cointaints a
# signature and description, per each unique UDF encountered

import datetime
import time

import requests
import pyvo
from pyvo.io.vosi.tapregext import TableAccess


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


class UDF:
    def __init__(self, form, description, source):
        """Metadata for an ADQL user defined function.

        It is constructed with form and description from the UDF
        description in the capability and the base URI of the TAP
        service it was found in.
        """
        self.form, self.description = form, description
        self.source = source


def get_udf_langfeature(service):
    """returns the list of ADQL language features for service.

    If there is multiple capabilities with ADQL UDFs, only the
    first will be returned.
    """
    for capability in service.capabilities:
        if isinstance(capability, TableAccess):
            for language in capability.languages:
                if language.name!="ADQL":
                    continue
                for langfeatlist in language.languagefeaturelists:
                    if (langfeatlist.type.lower()!=
                            'ivo://ivoa.net/std/tapregext#features-udf'):
                        continue
                    return langfeatlist
    return []


def get_udfs_for_service(service):
    """yields (form, description) pairs for the UDFs of a TAPService.
    """
    for feature in get_udf_langfeature(service):
        if feature.form.strip().startswith("ivo_"):
            continue
        yield UDF(
            feature.form,
            feature.description,
            service.baseurl)


def get_uniqued_udfs():
    """returns a sequence of UDF instances for all non ivo_ UDFs in
    the VO.

    This sequence is unique per form; hence, if multiple services define
    a UDF, only the first occurrences is retained.  To ensure that
    "first" does not change on every run, the services are queried in
    alphabetical order of their short names.

    This function does quite a bit of user interaction.
    """
    udfs_found = {}

    # we're sorting the services in order to have a predictable sequence,
    # which in turn should keep diffs regarding the sources of the UDFs
    # short most of the time.
    for service_record in sorted(
            pyvo.registry.search(servicetype='tap'),
            key=lambda rec: rec.short_name):
        print("Querying service {}...".format(service_record.short_name))
        try:
            for udf in get_udfs_for_service(
                    service_record.get_service("tap")):
                if udf.form not in udfs_found:
                    udfs_found[udf.form] = udf

        except KeyboardInterrupt:
            print("   ...skipped")
            # let users ^C out if they want
            time.sleep(0.5)

        except Exception as exc:
            print(f"    ...failed ({exc})")

    return udfs_found.values()


def main():
    udfs = sorted(get_uniqued_udfs(), key=lambda udf: udf.form)

    with open(FILE_NAME, 'w') as output_file:
        output_file.write(FILE_TITLE + "\n")
        output_file.write("*" * len(FILE_TITLE) + '\n\n')
        output_file.write("Generated with ``collect_adql_udf.py``\n\n")
        output_file.write("Last generated: " +
                          datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") +
                          "\n\n")
        for udf_item in udfs:
            udf_form = udf_item.form
            udf_desc = udf_item.description
            output_file.write("``" + udf_form + "``" + '\n')
            output_file.write("^" * (len(udf_form) + 4) + "\n\n")
            if udf_desc is not None:
                output_file.write(udf_desc + "\n\n")
            output_file.write(f"Try it on: {udf_item.source}\n\n")


if __name__=="__main__":
    main()
