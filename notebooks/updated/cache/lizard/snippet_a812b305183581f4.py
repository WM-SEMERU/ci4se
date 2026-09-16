def cql_encode_float(self, val):
    if math.isinf(val):
        return 'Infinity' if val > 0 else '-Infinity'
    elif math.isnan(val):
        return 'NaN'
    else:
        return repr(val)