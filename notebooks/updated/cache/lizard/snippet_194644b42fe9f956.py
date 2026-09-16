def _find_matching_instance(cache_key):
    infos = get_all()
    candidates = [info for info in infos if info.cache_key == cache_key]
    for candidate in sorted(candidates, key=lambda x: x.port):
        return candidate
    return None