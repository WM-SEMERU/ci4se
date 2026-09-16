def _from_python(self, value):
    if hasattr(value, 'strftime'):
        if hasattr(value, 'hour'):
            offset = value.utcoffset()
            if offset:
                value = value - offset
            value = value.replace(tzinfo=None).isoformat() + 'Z'
        else:
            value = '%sT00:00:00Z' % value.isoformat()
    elif isinstance(value, bool):
        if value:
            value = 'true'
        else:
            value = 'false'
    else:
        if IS_PY3:
            if isinstance(value, bytes):
                value = str(value, errors='replace')
        elif isinstance(value, str):
            value = unicode(value, errors='replace')
        value = '{0}'.format(value)
    return clean_xml_string(value)