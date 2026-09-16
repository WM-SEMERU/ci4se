def is_url(default_scheme='http', **kwargs):

    def converter(value):
        if value is None:
            return value
        if '://' not in value and default_scheme:
            value = '://'.join((default_scheme, value.strip()))
        try:
            return uris.validate(value)
        except uris.ValidationError as e:
            raise Invalid(e.message)
    return converter