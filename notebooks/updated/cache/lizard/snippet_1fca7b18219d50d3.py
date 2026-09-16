def get_tuple_version(name, default=DEFAULT_TUPLE_NOT_FOUND,
    allow_ambiguous=True):

    def _prefer_int(x):
        try:
            return int(x)
        except ValueError:
            return x
    version = get_string_version(name, default=default, allow_ambiguous=
        allow_ambiguous)
    if isinstance(version, tuple):
        return version
    return tuple(map(_prefer_int, version.split('.')))