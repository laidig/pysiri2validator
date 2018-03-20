#!/usr/bin/python3
"""
Python functions to validate SIRI 2.0 formatted XML
much credit to https://gist.github.com/iiska/215879
"""

import lxml
from lxml import etree


def getLoadedSchema(schemafile):
    doc = etree.parse(schemafile)
    try:
        schema = etree.XMLSchema(doc) 
    except Exception as e:
        print(e)
        exit(1)

    return schema


def parsebytes(schema, bytes):
    """ returns True if valid to XSD"""

    print("Validating")
    doc = etree.XML(bytes)
    return assertSchema(schema, doc)


def parseFile(schema, xml):
    """ returns True if valid to XSD"""

    print("Validating")
    doc = etree.parse(xml)
    return assertSchema(schema, doc)


def assertSchema(schema, doc):
    try:
        schema.assertValid(doc)
    except lxml.etree.DocumentInvalid as e:                                     
        print(e)
        return False
    return True
