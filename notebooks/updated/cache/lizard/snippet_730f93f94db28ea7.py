def load_xmlobject_from_string(string, xmlclass=XmlObject, validate=False,
    resolver=None):
    parser = _get_xmlparser(xmlclass=xmlclass, validate=validate, resolver=
        resolver)
    element = etree.fromstring(string, parser)
    return xmlclass(element)