def create_linear(num_finite_buckets, width, offset):
    if num_finite_buckets <= 0:
        raise ValueError(_BAD_NUM_FINITE_BUCKETS)
    if width <= 0.0:
        raise ValueError(_BAD_FLOAT_ARG % ('width', 0.0))
    return sc_messages.Distribution(bucketCounts=[0] * (num_finite_buckets +
        2), linearBuckets=sc_messages.LinearBuckets(numFiniteBuckets=
        num_finite_buckets, width=width, offset=offset))