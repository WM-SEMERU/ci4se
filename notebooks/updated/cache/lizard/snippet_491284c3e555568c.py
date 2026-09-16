def _get_from_cache(self, expr):
    try:
        is_cached = expr in self.cache
    except TypeError:
        is_cached = False
    if is_cached:
        return True, self.cache[expr]
    else:
        return False, None