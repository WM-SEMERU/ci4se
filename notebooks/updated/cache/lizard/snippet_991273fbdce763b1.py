def _get_feed_cache(self):
    feed_cache = None
    if os.path.exists(self._feed_cache_file):
        maxage = datetime.now() - timedelta(minutes=self._cachetime)
        file_ts = datetime.fromtimestamp(os.stat(self._feed_cache_file).
            st_mtime)
        if file_ts > maxage:
            try:
                with open(self._feed_cache_file, 'rb') as cache:
                    feed_cache = cache.read()
            finally:
                pass
    return feed_cache