def search_payload(self, fields=None, query=None):
    if fields is None:
        fields = set(self.get_values().keys())
    if query is None:
        query = {}
    payload = {}
    fields_dict = self.get_fields()
    for field in fields:
        value = getattr(self, field)
        if isinstance(fields_dict[field], OneToOneField):
            payload[field + '_id'] = value.id
        elif isinstance(fields_dict[field], OneToManyField):
            payload[field + '_ids'] = [entity.id for entity in value]
        else:
            payload[field] = value
    payload.update(query)
    return payload