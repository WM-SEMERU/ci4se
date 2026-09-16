def read_xso(src, xsomap):
    xso_parser = xso.XSOParser()
    for class_, cb in xsomap.items():
        xso_parser.add_class(class_, cb)
    driver = xso.SAXDriver(xso_parser)
    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, True)
    parser.setFeature(xml.sax.handler.feature_external_ges, False)
    parser.setContentHandler(driver)
    parser.parse(src)