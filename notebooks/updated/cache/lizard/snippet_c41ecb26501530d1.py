def getInterfacesFromXML(xmlStr, replaceKnownInterfaces=False):
    handler = IntrospectionHandler(replaceKnownInterfaces)
    xmlStr = xmlStr.strip()
    if xmlStr.startswith('<!DOCTYPE'):
        xmlStr = xmlStr[xmlStr.find('>') + 1:]
    p = xml.sax.make_parser()
    p.setFeature(xml.sax.handler.feature_validation, False)
    p.setFeature(xml.sax.handler.feature_external_ges, False)
    p.setContentHandler(handler)
    p.parse(cStringIO(xmlStr))
    return handler.interfaces