def _convert_from(data):
    try:
        module, klass_name = data['__class__'].rsplit('.', 1)
        klass = getattr(import_module(module), klass_name)
    except (ImportError, AttributeError, KeyError):
        return data
    return deserialize(klass, data['__value__'])