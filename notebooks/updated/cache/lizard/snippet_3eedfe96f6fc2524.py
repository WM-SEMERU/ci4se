def _deserialize(self, value, attr, data):
    value = super(SanitizedHTML, self)._deserialize(value, attr, data)
    return bleach.clean(value, tags=self.tags, attributes=self.attrs, strip
        =True).strip()