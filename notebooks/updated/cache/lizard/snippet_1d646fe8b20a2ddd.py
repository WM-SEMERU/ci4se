def should_series_dispatch(left, right, op):
    if left._is_mixed_type or right._is_mixed_type:
        return True
    if not len(left.columns) or not len(right.columns):
        return False
    ldtype = left.dtypes.iloc[0]
    rdtype = right.dtypes.iloc[0]
    if is_timedelta64_dtype(ldtype) and is_integer_dtype(rdtype
        ) or is_timedelta64_dtype(rdtype) and is_integer_dtype(ldtype):
        return True
    if is_datetime64_dtype(ldtype) and is_object_dtype(rdtype):
        return True
    return False