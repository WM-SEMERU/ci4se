def stream_time(self, significant_digits=3):
    try:
        return round(self._timestamps['last_stream'] - self._timestamps[
            'stream'], significant_digits)
    except Exception as e:
        return None