def unpack_datetime(self, data):
    if data is None:
        return None
    try:
        value = CIMDateTime(data)
    except ValueError as exc:
        raise CIMXMLParseError(_format(
            'Invalid datetime value: {0!A} ({1})', data, exc), conn_id=self
            .conn_id)
    return value