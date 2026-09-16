def bucket(arg, buckets, closed='left', close_extreme=True, include_under=
    False, include_over=False):
    op = Bucket(arg, buckets, closed=closed, close_extreme=close_extreme,
        include_under=include_under, include_over=include_over)
    return op.to_expr()