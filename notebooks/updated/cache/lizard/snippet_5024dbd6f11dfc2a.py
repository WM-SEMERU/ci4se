def writeKerning(self, location=None, masters=None):
    if self.currentInstance is None:
        return
    kerningElement = ET.Element('kerning')
    if location is not None:
        locationElement = self._makeLocationElement(location)
        kerningElement.append(locationElement)
    self.currentInstance.append(kerningElement)