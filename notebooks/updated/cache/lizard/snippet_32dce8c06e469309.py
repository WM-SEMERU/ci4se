def save_xml(self, doc, element):
    element.setAttributeNS(RTS_EXT_NS, RTS_EXT_NS_S + 'x', str(self.x))
    element.setAttributeNS(RTS_EXT_NS, RTS_EXT_NS_S + 'y', str(self.y))
    element.setAttributeNS(RTS_EXT_NS, RTS_EXT_NS_S + 'height', str(self.
        height))
    element.setAttributeNS(RTS_EXT_NS, RTS_EXT_NS_S + 'width', str(self.width))
    element.setAttributeNS(RTS_EXT_NS, RTS_EXT_NS_S + 'direction', dir.
        to_string(self.direction).lower())