def __add_text(self, text):
    if text is not None and not isinstance(text, six.text_type):
        raise TypeError(
            'Local symbol definition must be a Unicode sequence or None: %r' %
            text)
    sid = self.__new_sid()
    location = None
    if self.table_type.is_shared:
        location = self.__import_location(sid)
    token = SymbolToken(text, sid, location)
    self.__add(token)
    return token