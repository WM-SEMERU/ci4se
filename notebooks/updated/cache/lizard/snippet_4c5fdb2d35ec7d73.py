def get_fields_for_keyword(self, keyword, mode='a'):
    field = self.keyword_to_fields.get(keyword, keyword)
    if isinstance(field, dict):
        return field[mode]
    elif isinstance(field, (list, tuple)):
        return field
    return [field]