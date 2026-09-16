def autohash(include=None, exclude=None, only_constructor_args=False,
    only_public_fields=False, cls=DECORATED):
    return autohash_decorate(cls, include=include, exclude=exclude,
        only_constructor_args=only_constructor_args, only_public_fields=
        only_public_fields)