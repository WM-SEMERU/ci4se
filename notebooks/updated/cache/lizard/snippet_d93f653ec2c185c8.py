def certify_bytes(value, min_length=None, max_length=None, required=True):
    certify_params((_certify_int_param, 'min_value', min_length, dict(
        negative=False, required=False)), (_certify_int_param, 'max_value',
        max_length, dict(negative=False, required=False)))
    if certify_required(value=value, required=required):
        return
    if not isinstance(value, six.binary_type):
        raise CertifierTypeError(message=
            'expected byte string, but value is of type {cls!r}'.format(cls
            =value.__class__.__name__), value=value, required=required)
    if min_length is not None and len(value) < min_length:
        raise CertifierValueError(message=
            '{length} is shorter than minimum acceptable {min}'.format(
            length=len(value), min=min_length), value=value, required=required)
    if max_length is not None and len(value) > max_length:
        raise CertifierValueError(message=
            '{length} is longer than maximum acceptable {max}'.format(
            length=len(value), max=max_length), value=value, required=required)