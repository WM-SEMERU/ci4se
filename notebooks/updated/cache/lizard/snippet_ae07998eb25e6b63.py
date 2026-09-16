def _read_uaa_cache(self):
    self._cache_path = os.path.expanduser('~/.predix/uaa.json')
    if not os.path.exists(self._cache_path):
        return self._initialize_uaa_cache()
    with open(self._cache_path, 'r') as data:
        return json.load(data)