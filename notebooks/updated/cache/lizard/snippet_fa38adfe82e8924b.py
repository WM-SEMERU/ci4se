def get_fields(brain_or_object):
    obj = get_object(brain_or_object)
    schema = get_schema(obj)
    if is_dexterity_content(obj):
        names = schema.names()
        fields = map(lambda name: schema.get(name), names)
        return dict(zip(names, fields))
    return dict(zip(schema.keys(), schema.fields()))