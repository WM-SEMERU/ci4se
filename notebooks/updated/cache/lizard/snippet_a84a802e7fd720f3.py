def newround(number, ndigits=None):
    return_int = False
    if ndigits is None:
        return_int = True
        ndigits = 0
    if hasattr(number, '__round__'):
        return number.__round__(ndigits)
    if ndigits < 0:
        raise NotImplementedError('negative ndigits not supported yet')
    exponent = Decimal('10') ** -ndigits
    if PYPY:
        if 'numpy' in repr(type(number)):
            number = float(number)
    if not PY26:
        d = Decimal.from_float(number).quantize(exponent, rounding=
            ROUND_HALF_EVEN)
    else:
        d = from_float_26(number).quantize(exponent, rounding=ROUND_HALF_EVEN)
    if return_int:
        return int(d)
    else:
        return float(d)