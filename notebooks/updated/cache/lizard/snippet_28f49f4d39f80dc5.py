def arbitrary_object_to_string(a_thing):
    if a_thing is None:
        return ''
    if isinstance(a_thing, six.string_types):
        return a_thing
    if six.PY3 and isinstance(a_thing, six.binary_type):
        try:
            return a_thing.decode('utf-8')
        except UnicodeDecodeError:
            pass
    try:
        return a_thing.to_str()
    except (AttributeError, KeyError, TypeError):
        pass
    try:
        return arbitrary_object_to_string(a_thing.a_type)
    except (AttributeError, KeyError, TypeError):
        pass
    try:
        return known_mapping_type_to_str[a_thing]
    except (KeyError, TypeError):
        pass
    try:
        if a_thing.__module__ not in ('__builtin__', 'builtins', 'exceptions'):
            if a_thing.__module__ == '__main__':
                module_name = sys.modules['__main__'].__file__[:-3].replace('/'
                    , '.').strip('.')
            else:
                module_name = a_thing.__module__
            return '%s.%s' % (module_name, a_thing.__name__)
    except AttributeError:
        pass
    try:
        return a_thing.__name__
    except AttributeError:
        pass
    return str(a_thing)