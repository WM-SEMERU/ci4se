def _int_to_datetime(expr):
    if isinstance(expr, SequenceExpr):
        return IntToDatetime(_input=expr, _data_type=types.datetime)
    elif isinstance(expr, Scalar):
        return IntToDatetime(_input=expr, _value_type=types.datetime)