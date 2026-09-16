def to_xml(self, xml_declaration=True):
    xml = ET.tostring(self.xml()).decode('utf-8')
    return '<?xml version="1.0" encoding="UTF-8"?>{}'.format(xml
        ) if xml_declaration else xml