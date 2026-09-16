def _version_header(self):
    if not self._cached_version_header:
        self._cached_version_header = urlparse.urlencode(self._version_values()
            )
    return self._cached_version_header