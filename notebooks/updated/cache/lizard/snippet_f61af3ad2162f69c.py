def get_field_mapping(self):
    field_mapping = self.field_mapping_widget.get_field_mapping()
    for k, v in list(field_mapping['values'].items()):
        if not v:
            field_mapping['values'].pop(k)
    for k, v in list(field_mapping['fields'].items()):
        if not v:
            field_mapping['fields'].pop(k)
    return field_mapping