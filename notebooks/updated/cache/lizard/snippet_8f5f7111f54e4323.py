def create_gnu_header(self, info, encoding, errors):
    info['magic'] = GNU_MAGIC
    buf = b''
    if len(info['linkname']) > LENGTH_LINK:
        buf += self._create_gnu_long_header(info['linkname'],
            GNUTYPE_LONGLINK, encoding, errors)
    if len(info['name']) > LENGTH_NAME:
        buf += self._create_gnu_long_header(info['name'], GNUTYPE_LONGNAME,
            encoding, errors)
    return buf + self._create_header(info, GNU_FORMAT, encoding, errors)