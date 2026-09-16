def get_fields(self, serializer_fields):
    fields = OrderedDict()
    for field_name, field in serializer_fields.items():
        if field_name == 'tags':
            continue
        info = self.get_field_info(field, field_name)
        if info:
            fields[field_name] = info
    return fields