def toUnicode(data, encoding=DEFAULT_ENCODING):
    if isinstance(data, unicode_type):
        return data
    if isinstance(data, bytes_type):
        return unicode_type(data, encoding=encoding)
    if hasattr(data, '__iter__'):
        try:
            dict(data)
        except TypeError:
            pass
        except ValueError:
            return (toUnicode(i, encoding) for i in data)
        else:
            if hasattr(data, 'items'):
                data = data.items()
            return dict((toUnicode(k, encoding), toUnicode(v, encoding)) for
                k, v in data)
    return data