def parse(self, fn):
    ioc_xml = xmlutils.read_xml_no_ns(fn)
    if not ioc_xml:
        return False
    root = ioc_xml.getroot()
    iocid = root.get('id', None)
    if not iocid:
        return False
    self.iocs[iocid] = ioc_xml
    return True