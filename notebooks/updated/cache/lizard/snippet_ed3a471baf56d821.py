def compile(self, source, name=None, filename=None, raw=False, defer_init=False
    ):
    source_hint = None
    try:
        if isinstance(source, string_types):
            source_hint = source
            source = self._parse(source, name, filename)
        source = self._generate(source, name, filename, defer_init=defer_init)
        if raw:
            return source
        if filename is None:
            filename = '<template>'
        else:
            filename = encode_filename(filename)
        return self._compile(source, filename)
    except TemplateSyntaxError:
        exc_info = sys.exc_info()
    self.handle_exception(exc_info, source_hint=source_hint)