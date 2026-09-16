def _base_body(self):
    item_attrib = {'xmlns:s': 'http://schemas.xmlsoap.org/soap/envelope/'}
    xml = XML.Element('s:Envelope', item_attrib)
    XML.SubElement(xml, 's:Header')
    item_attrib = {'xmlns': 'http://www.sonos.com/Services/1.1'}
    credentials = XML.SubElement(xml[0], 'credentials', item_attrib)
    XML.SubElement(credentials, 'sessionId').text = self._session_id
    XML.SubElement(credentials, 'deviceId').text = self._serial_number
    XML.SubElement(credentials, 'deviceProvider').text = 'Sonos'
    return xml