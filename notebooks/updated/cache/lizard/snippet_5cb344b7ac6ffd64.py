def parse_named_unicode(self, i):
    value = ord(_unicodedata.lookup(self.get_named_unicode(i)))
    single = self.get_single_stack()
    if self.span_stack:
        text = self.convert_case(chr(value), self.span_stack[-1])
        value = ord(self.convert_case(text, single)
            ) if single is not None else ord(text)
    elif single:
        value = ord(self.convert_case(chr(value), single))
    if self.use_format and value in _CURLY_BRACKETS_ORD:
        self.handle_format(chr(value), i)
    elif value <= 255:
        self.result.append('\\%03o' % value)
    else:
        self.result.append(chr(value))