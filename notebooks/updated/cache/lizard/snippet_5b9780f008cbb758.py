def get_time_buckets(start, end):
    d = DatalakeRecord.TIME_BUCKET_SIZE_IN_MS
    first_bucket = start / d
    last_bucket = end / d
    return list(range(int(first_bucket), int(last_bucket) + 1))