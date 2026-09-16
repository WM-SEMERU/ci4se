def _makeLocationElement(self, locationObject, name=None):
    locElement = ET.Element('location')
    if name is not None:
        locElement.attrib['name'] = name
    for dimensionName, dimensionValue in locationObject.items():
        dimElement = ET.Element('dimension')
        dimElement.attrib['name'] = dimensionName
        if type(dimensionValue) == tuple:
            dimElement.attrib['xvalue'] = '%f' % dimensionValue[0]
            dimElement.attrib['yvalue'] = '%f' % dimensionValue[1]
        else:
            dimElement.attrib['xvalue'] = '%f' % dimensionValue
        locElement.append(dimElement)
    return locElement