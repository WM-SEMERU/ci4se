def dict_to_xml(spec, full_document=False):
    middle = xmltodict.unparse(spec, full_document=full_document, pretty=True)
    return lxml.etree.fromstring(middle)