def _update_exponential_bucket_count(a_float, dist):
    buckets = dist.exponentialBuckets
    if buckets is None:
        raise ValueError(_BAD_UNSET_BUCKETS % 'exponential buckets')
    bucket_counts = dist.bucketCounts
    num_finite_buckets = buckets.numFiniteBuckets
    if len(bucket_counts) < num_finite_buckets + 2:
        raise ValueError(_BAD_LOW_BUCKET_COUNT)
    scale = buckets.scale
    factor = buckets.growthFactor
    if a_float <= scale:
        index = 0
    else:
        index = 1 + int(math.log(a_float / scale) / math.log(factor))
        index = min(index, num_finite_buckets + 1)
    bucket_counts[index] += 1
    _logger.debug('scale:%f, factor:%f, sample:%f, index:%d', scale, factor,
        a_float, index)