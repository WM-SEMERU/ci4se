def print_model(self, pretty=True, encoding='utf8'):
    return lxml.etree.tostring(self.sbgn, pretty_print=pretty, encoding=
        encoding, xml_declaration=True)