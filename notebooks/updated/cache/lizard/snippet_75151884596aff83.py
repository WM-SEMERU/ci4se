def all_default_fields():
    default_fields = []
    for item in dir(fields):
        if not item.startswith('__'):
            var = getattr(definitions, item)
            if isinstance(var, dict):
                if var.get('replace_null', False):
                    default_fields.append(var)
    return default_fields