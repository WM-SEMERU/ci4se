def save_xml(self, doc, element):
    element.setAttributeNS(XSI_NS, XSI_NS_S + 'type', 'rtsExt:serviceport_ext')
    element.setAttributeNS(RTS_NS, RTS_NS_S + 'name', self.name)
    if self.comment:
        element.setAttributeNS(RTS_EXT_NS, RTS_EXT_NS_S + 'comment', self.
            comment)
    if self.visible != True:
        element.setAttributeNS(RTS_EXT_NS, RTS_EXT_NS_S + 'visible', str(
            self.visible).lower())
    for p in self.properties:
        new_prop_element = doc.createElementNS(RTS_EXT_NS, RTS_EXT_NS_S +
            'Properties')
        properties_to_xml(new_prop_element, p, self.properties[p])
        element.appendChild(new_prop_element)