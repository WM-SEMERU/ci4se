def field_items(self, path=str(), **options):
    items = list()
    items.append((path if path else 'field', self))
    data_path = '{0}.{1}'.format(path, 'data') if path else 'data'
    if is_container(self._data):
        for field_item in self._data.field_items(data_path, **options):
            items.append(field_item)
    elif is_pointer(self._data) and get_nested(options):
        for field_item in self._data.field_items(data_path, **options):
            items.append(field_item)
    elif is_field(self._data):
        items.append((data_path, self._data))
    return items