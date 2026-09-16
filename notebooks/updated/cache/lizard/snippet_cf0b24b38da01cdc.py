def _bucket_boundaries(max_length, min_length=8, length_bucket_step=1.1):
    assert length_bucket_step > 1.0
    x = min_length
    boundaries = []
    while x < max_length:
        boundaries.append(x)
        x = max(x + 1, int(x * length_bucket_step))
    return boundaries