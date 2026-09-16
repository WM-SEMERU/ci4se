def compute_and_cache_missing_buckets(self, start_time, end_time,
    untrusted_time, force_recompute=False):
    if untrusted_time and not untrusted_time.tzinfo:
        untrusted_time = untrusted_time.replace(tzinfo=tzutc())
    events = self._compute_buckets(start_time, end_time, compute_missing=
        True, cache=True, untrusted_time=untrusted_time, force_recompute=
        force_recompute)
    for event in events:
        yield event