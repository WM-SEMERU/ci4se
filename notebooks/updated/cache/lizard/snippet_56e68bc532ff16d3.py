def get_instance(name, provider=None):
    data = action(fun='show_instance', names=[name], provider=provider)
    info = salt.utils.data.simple_types_filter(data)
    try:
        info = next(six.itervalues(next(six.itervalues(next(six.itervalues(
            info))))))
    except AttributeError:
        return None
    return info