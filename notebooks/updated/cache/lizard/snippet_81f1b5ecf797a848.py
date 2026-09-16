def unpack_char16(self, data):
    if data is None:
        return None
    len_data = len(data)
    if len_data == 0:
        raise CIMXMLParseError('Char16 value is empty', conn_id=self.conn_id)
    if len_data > 1:
        raise CIMXMLParseError(_format(
            'Char16 value has more than one UCS-2 character: {0!A}', data),
            conn_id=self.conn_id)
    if ord(data) > 65535:
        raise CIMXMLParseError(_format(
            'Char16 value is a character outside of the UCS-2 range: {0!A}',
            data), conn_id=self.conn_id)
    return data