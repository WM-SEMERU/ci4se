def pk_names(cls):
    if cls._cache_pk_names is None:
        cls._cache_pk_names = cls._get_primary_key_names()
    return cls._cache_pk_names