def named_object(name):
    name_parts = name.split('.')
    module = named_module('.'.join(name_parts[:-1]))
    return getattr(module, name_parts[-1])