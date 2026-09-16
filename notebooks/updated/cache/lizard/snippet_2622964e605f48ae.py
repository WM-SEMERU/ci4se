def parse_encoding(value=None):
    if value is None:
        return ca_settings.CA_DEFAULT_ENCODING
    elif isinstance(value, Encoding):
        return value
    elif isinstance(value, six.string_types):
        if value == 'ASN1':
            value = 'DER'
        try:
            return getattr(Encoding, value)
        except AttributeError:
            raise ValueError('Unknown encoding: %s' % value)
    else:
        raise ValueError('Unknown type passed: %s' % type(value).__name__)