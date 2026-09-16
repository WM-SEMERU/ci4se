def op_count(cls, crawler, stage=None):
    if stage:
        total_ops = conn.get(make_key(crawler, stage))
    else:
        total_ops = conn.get(make_key(crawler, 'total_ops'))
    return unpack_int(total_ops)