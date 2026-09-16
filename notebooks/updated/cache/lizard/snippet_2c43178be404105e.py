def convert(credentials):
    credentials_class = type(credentials)
    try:
        return _CLASS_CONVERSION_MAP[credentials_class](credentials)
    except KeyError as caught_exc:
        new_exc = ValueError(_CONVERT_ERROR_TMPL.format(credentials_class))
        six.raise_from(new_exc, caught_exc)