#!/usr/bin/python3

"""
validate SIRI2.0 XML
"""
import sys
from urllib.parse import urlparse
import requests
from functions import getLoadedSchema, parsebytes, parseFile

SCHEMA_FILE = './xsd_minified/siriSg.xsd'

if __name__ == "__main__":
    schema = getLoadedSchema(SCHEMA_FILE)

    fileOrHttp = sys.argv[1]

    if urlparse(fileOrHttp).scheme in ('http', 'https',):
        r = requests.get(fileOrHttp)
        print("loading " + fileOrHttp)
        result = parsebytes(schema, r.content)

    else:
        with open(fileOrHttp) as f:
            result = parseFile(schema, f)

    if result:
        print("Valid SIRI")

