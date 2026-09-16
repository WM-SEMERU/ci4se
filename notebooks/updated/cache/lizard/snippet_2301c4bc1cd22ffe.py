def get_fields(model, include=None):
    fields = OrderedDict()
    info = model._meta
    if include:
        selected = [info.get_field(name) for name in include]
    else:
        selected = [field for field in info.fields if field.editable]
    for field in selected:
        fields[field.name] = field.verbose_name
    return fields