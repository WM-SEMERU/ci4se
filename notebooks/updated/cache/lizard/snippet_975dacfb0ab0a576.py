def to_XML(self, xml_declaration=True, xmlns=True):
    root_node = self._to_DOM()
    if xmlns:
        xmlutils.annotate_with_XMLNS(root_node, LOCATION_XMLNS_PREFIX,
            LOCATION_XMLNS_URL)
    return xmlutils.DOM_node_to_XML(root_node, xml_declaration)