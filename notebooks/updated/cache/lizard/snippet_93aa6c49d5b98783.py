def get_xml(self, encoding='unicode'):
    return xml.etree.ElementTree.tostring(self._root_el, encoding)