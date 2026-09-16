def store_magic_envelope_doc(self, payload):
    try:
        json_payload = json.loads(decode_if_bytes(payload))
    except ValueError:
        xml = unquote(decode_if_bytes(payload))
        xml = xml.lstrip().encode('utf-8')
        logger.debug(
            'diaspora.protocol.store_magic_envelope_doc: xml payload: %s', xml)
        self.doc = etree.fromstring(xml)
    else:
        logger.debug(
            'diaspora.protocol.store_magic_envelope_doc: json payload: %s',
            json_payload)
        self.doc = self.get_json_payload_magic_envelope(json_payload)