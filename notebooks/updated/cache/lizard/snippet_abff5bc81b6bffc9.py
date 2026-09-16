def serialize(self):
    data = {}
    for field_name in self.get_statement_field_names():
        format_method = getattr(self, 'get_{}'.format(field_name), None)
        if format_method:
            data[field_name] = format_method()
        else:
            data[field_name] = getattr(self, field_name)
    return data