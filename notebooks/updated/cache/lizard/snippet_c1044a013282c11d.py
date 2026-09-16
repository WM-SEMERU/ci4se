def writeObject(self, o):
    if self.writeReference(o) != -1:
        return
    self.context.addObject(o)
    alias = self.context.getClassAlias(o.__class__)
    alias.compile()
    if alias.amf3:
        self.writeAMF3(o)
        return
    if alias.anonymous:
        self.writeType(TYPE_OBJECT)
    else:
        self.writeType(TYPE_TYPEDOBJECT)
        self.serialiseString(alias.alias)
    attrs = alias.getEncodableAttributes(o, codec=self)
    if alias.static_attrs and attrs:
        for key in alias.static_attrs:
            value = attrs.pop(key)
            self.serialiseString(key)
            self.writeElement(value)
    if attrs:
        self._writeDict(attrs)
    self._writeEndObject()