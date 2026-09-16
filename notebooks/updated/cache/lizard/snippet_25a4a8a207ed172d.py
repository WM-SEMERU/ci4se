def from_filename(cls, filename):
    result = cls._FROM_FILENAME_CACHE.get(filename)
    if result is None:
        result = cls(cls._normalize(filename))
        cls._FROM_FILENAME_CACHE.store(filename, result)
    return result