def ean13(self, data, **kwargs):
    if not re.match('\\d{13}', data):
        raise ValueError(
            'JAN-13/EAN-13 symbology requires 13 digits of data; got {:d} digits: {!r}'
            .format(len(data), data))
    barcode.validate_barcode_args(**kwargs)
    return self._ean13_impl(data, **kwargs)