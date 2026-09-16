def from_string(cls, jss, xml_string):
    root = ElementTree.fromstring(xml_string.encode('utf-8'))
    return cls(jss, root)