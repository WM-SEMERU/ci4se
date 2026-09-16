def sourcelines(self):
    source = None
    if self.loader is not None:
        try:
            if hasattr(self.loader, 'get_source'):
                source = self.loader.get_source(self.module)
            elif hasattr(self.loader, 'get_source_by_code'):
                source = self.loader.get_source_by_code(self.code)
        except Exception:
            pass
    if source is None:
        try:
            f = open(self.filename)
        except IOError:
            return []
        try:
            source = f.read()
        finally:
            f.close()
    if isinstance(source, str):
        return source.splitlines()
    charset = 'utf-8'
    if source.startswith(UTF8_COOKIE):
        source = source[3:]
    else:
        for idx, match in enumerate(_line_re.finditer(source)):
            match = _line_re.search(match.group())
            if match is not None:
                charset = match.group(1)
                break
            if idx > 1:
                break
    try:
        codecs.lookup(charset)
    except LookupError:
        charset = 'utf-8'
    return source.decode(charset, 'replace').splitlines()