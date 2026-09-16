def _has_xml_encode(self, content):
    encode = None
    m = RE_XML_START.match(content)
    if m:
        if m.group(1):
            m2 = RE_XML_ENCODE.match(m.group(1))
            if m2:
                enc = m2.group(2).decode('ascii')
                try:
                    codecs.getencoder(enc)
                    encode = enc
                except LookupError:
                    pass
        else:
            if m.group(2):
                enc = 'utf-32-be'
                text = m.group(2)
            elif m.group(3):
                enc = 'utf-32-le'
                text = m.group(3)
            elif m.group(4):
                enc = 'utf-16-be'
                text = m.group(4)
            elif m.group(5):
                enc = 'utf-16-le'
                text = m.group(5)
            try:
                m2 = RE_XML_ENCODE_U.match(text.decode(enc))
            except Exception:
                m2 = None
            if m2:
                enc = m2.group(2)
                try:
                    codecs.getencoder(enc)
                    encode = enc
                except Exception:
                    pass
    return encode