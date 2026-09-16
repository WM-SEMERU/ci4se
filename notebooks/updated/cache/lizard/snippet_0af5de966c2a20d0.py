def get_next_interval_histogram(self, range_start_time_sec=0.0,
    range_end_time_sec=sys.maxsize, absolute=False):
    return self._decode_next_interval_histogram(None, range_start_time_sec,
        range_end_time_sec, absolute)