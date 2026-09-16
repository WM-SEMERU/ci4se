def current(self, fields=None):
    if fields is None:
        fields = self.fields
    return dict((f, self.get_field_value(f)) for f in fields)