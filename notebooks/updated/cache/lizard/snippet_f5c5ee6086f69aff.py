def _proc_pax(self, filetar):
    buf = filetar.fileobj.read(self._block(self.size))
    if self.type == tarfile.XGLTYPE:
        pax_headers = filetar.pax_headers
    else:
        pax_headers = filetar.pax_headers.copy()
    regex = re.compile('(\\d+) ([^=]+)=', re.U)
    pos = 0
    while True:
        match = regex.match(buf, pos)
        if not match:
            break
        length, keyword = match.groups()
        length = int(length)
        value = buf[match.end(2) + 1:match.start(1) + length - 1]
        try:
            keyword = keyword.decode('utf8')
        except Exception:
            pass
        try:
            value = value.decode('utf8')
        except Exception:
            pass
        pax_headers[keyword] = value
        pos += length
    try:
        next = self.fromtarfile(filetar)
    except tarfile.HeaderError:
        raise tarfile.SubsequentHeaderError('missing or bad subsequent header')
    if self.type in (tarfile.XHDTYPE, tarfile.SOLARIS_XHDTYPE):
        next._apply_pax_info(pax_headers, filetar.encoding, filetar.errors)
        next.offset = self.offset
        if 'size' in pax_headers:
            offset = next.offset_data
            if next.isreg() or next.type not in tarfile.SUPPORTED_TYPES:
                offset += next._block(next.size)
            filetar.offset = offset
    return next