def writeInfo(self, location=None, masters=None):
    if self.currentInstance is None:
        return
    infoElement = ET.Element('info')
    if location is not None:
        locationElement = self._makeLocationElement(location)
        infoElement.append(locationElement)
    self.currentInstance.append(infoElement)