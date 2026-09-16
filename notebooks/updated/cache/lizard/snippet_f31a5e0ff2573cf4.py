def save_xml(self, doc, element):
    super(TargetPort, self).save_xml(doc, element)
    element.setAttributeNS(XSI_NS, XSI_NS_S + 'type', 'rtsExt:target_port_ext')
    element.setAttributeNS(RTS_NS, RTS_NS_S + 'portName', self.port_name)