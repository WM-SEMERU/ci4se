def getXML(self):
    s = ''
    for element in self._svgElements:
        s += element.getXML()
    return s