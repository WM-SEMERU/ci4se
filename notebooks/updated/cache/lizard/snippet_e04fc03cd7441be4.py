def convert_Decimal(x, encoder):
    if encoder.strict is False:
        return float(x)
    raise pyamf.EncodeError(
        'Unable to encode decimal.Decimal instances as there is no way to guarantee exact conversion. Use strict=False to convert to a float.'
        )