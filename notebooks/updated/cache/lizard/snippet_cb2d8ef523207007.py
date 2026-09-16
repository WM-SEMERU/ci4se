def format_array(values, formatter, float_format=None, na_rep='NaN', digits
    =None, space=None, justify='right', decimal='.', leading_space=None):
    if is_datetime64_dtype(values.dtype):
        fmt_klass = Datetime64Formatter
    elif is_datetime64tz_dtype(values):
        fmt_klass = Datetime64TZFormatter
    elif is_timedelta64_dtype(values.dtype):
        fmt_klass = Timedelta64Formatter
    elif is_extension_array_dtype(values.dtype):
        fmt_klass = ExtensionArrayFormatter
    elif is_float_dtype(values.dtype) or is_complex_dtype(values.dtype):
        fmt_klass = FloatArrayFormatter
    elif is_integer_dtype(values.dtype):
        fmt_klass = IntArrayFormatter
    else:
        fmt_klass = GenericArrayFormatter
    if space is None:
        space = get_option('display.column_space')
    if float_format is None:
        float_format = get_option('display.float_format')
    if digits is None:
        digits = get_option('display.precision')
    fmt_obj = fmt_klass(values, digits=digits, na_rep=na_rep, float_format=
        float_format, formatter=formatter, space=space, justify=justify,
        decimal=decimal, leading_space=leading_space)
    return fmt_obj.get_result()