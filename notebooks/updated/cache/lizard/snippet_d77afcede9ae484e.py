def lookup_generic(self, obj, as_of_date, country_code):
    matches = []
    missing = []
    if isinstance(obj, (AssetConvertible, ContinuousFuture)):
        self._lookup_generic_scalar(obj=obj, as_of_date=as_of_date,
            country_code=country_code, matches=matches, missing=missing)
        try:
            return matches[0], missing
        except IndexError:
            if hasattr(obj, '__int__'):
                raise SidsNotFound(sids=[obj])
            else:
                raise SymbolNotFound(symbol=obj)
    try:
        iterator = iter(obj)
    except TypeError:
        raise NotAssetConvertible(
            'Input was not a AssetConvertible or iterable of AssetConvertible.'
            )
    for obj in iterator:
        self._lookup_generic_scalar(obj=obj, as_of_date=as_of_date,
            country_code=country_code, matches=matches, missing=missing)
    return matches, missing