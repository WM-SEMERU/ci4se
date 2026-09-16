def _build_doc(self):
    from lxml.html import parse, fromstring, HTMLParser
    from lxml.etree import XMLSyntaxError
    parser = HTMLParser(recover=True, encoding=self.encoding)
    try:
        if _is_url(self.io):
            with urlopen(self.io) as f:
                r = parse(f, parser=parser)
        else:
            r = parse(self.io, parser=parser)
        try:
            r = r.getroot()
        except AttributeError:
            pass
    except (UnicodeDecodeError, IOError) as e:
        if not _is_url(self.io):
            r = fromstring(self.io, parser=parser)
            try:
                r = r.getroot()
            except AttributeError:
                pass
        else:
            raise e
    else:
        if not hasattr(r, 'text_content'):
            raise XMLSyntaxError('no text parsed from document', 0, 0, 0)
    return r