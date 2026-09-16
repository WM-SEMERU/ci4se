def assemble(self, header_json, metadata_json, content_json):
    header = json_decode(header_json)
    if 'msgtype' not in header:
        log.error('Bad header with no msgtype was: %r', header)
        raise ProtocolError("No 'msgtype' in header")
    return self._messages[header['msgtype']].assemble(header_json,
        metadata_json, content_json)