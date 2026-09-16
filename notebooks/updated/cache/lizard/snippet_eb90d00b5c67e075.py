def dumps(voevent, pretty_print=False, xml_declaration=True, encoding='UTF-8'):
    vcopy = copy.deepcopy(voevent)
    _return_to_standard_xml(vcopy)
    s = etree.tostring(vcopy, pretty_print=pretty_print, xml_declaration=
        xml_declaration, encoding=encoding)
    return s