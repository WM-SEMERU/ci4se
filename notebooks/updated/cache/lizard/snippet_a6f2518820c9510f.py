def code128(self, data, **kwargs):
    if not re.match('^[\\x20-\\x7F]+$', data):
        raise ValueError(
            'Invalid Code 128 symbology. Code 128 can encode any ASCII character ranging from 32 (20h) to 127 (7Fh); got {!r}'
            .format(data))
    codeset = kwargs.pop('codeset', barcode.CODE128_A)
    barcode.validate_barcode_args(**kwargs)
    return self._code128_impl(data, codeset=codeset, **kwargs)