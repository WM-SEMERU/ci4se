def get_cached(path, cache_name=None, **kwargs):
    if gw2api.cache_dir and gw2api.cache_time and cache_name is not False:
        if cache_name is None:
            cache_name = path
        cache_file = os.path.join(gw2api.cache_dir, cache_name)
        if mtime(cache_file) >= time.time() - gw2api.cache_time:
            with open(cache_file, 'r') as fp:
                return json.load(fp)
    else:
        cache_file = None
    r = gw2api.session.get(gw2api.BASE_URL + path, **kwargs)
    if not r.ok:
        try:
            response = r.json()
        except ValueError:
            response = None
        if isinstance(response, dict) and 'text' in response:
            r.reason = response['text']
    r.raise_for_status()
    data = r.json()
    if cache_file:
        with open(cache_file, 'w') as fp:
            json.dump(data, fp, indent=2)
    return data