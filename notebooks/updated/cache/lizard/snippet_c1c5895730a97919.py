def _get_indexes_by_path(self, field):
    try:
        field, next_field = field.split('.', 1)
    except ValueError:
        next_field = ''
    if field == '*':
        index_list = []
        for item in self:
            index_list.append(self.index(item))
        if index_list:
            return index_list, next_field
        return [], None
    elif field.isnumeric():
        index = int(field)
        if index >= len(self):
            return None, None
        return [index], next_field