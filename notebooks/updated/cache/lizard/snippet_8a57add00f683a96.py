def menuTemplate(self):
    xml = ElementTree.Element('menu')
    for i in range(self.uiMenuTREE.topLevelItemCount()):
        self.saveXml(xml, self.uiMenuTREE.topLevelItem(i))
    projex.text.xmlindent(xml)
    return ElementTree.tostring(xml)