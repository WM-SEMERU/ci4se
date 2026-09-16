def _buckets_nearly_equal(a_dist, b_dist):
    a_type, a_buckets = _detect_bucket_option(a_dist)
    b_type, b_buckets = _detect_bucket_option(b_dist)
    if a_type != b_type:
        return False
    elif a_type == 'linearBuckets':
        return _linear_buckets_nearly_equal(a_buckets, b_buckets)
    elif a_type == 'exponentialBuckets':
        return _exponential_buckets_nearly_equal(a_buckets, b_buckets)
    elif a_type == 'explicitBuckets':
        return _explicit_buckets_nearly_equal(a_buckets, b_buckets)
    else:
        return False