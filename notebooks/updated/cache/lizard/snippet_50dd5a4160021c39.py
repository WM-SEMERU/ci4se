def _lookup_unconflicted_symbol(self, symbol):
    try:
        uppered = symbol.upper()
    except AttributeError:
        return numpy.nan
    try:
        return self.finder.lookup_symbol(uppered, as_of_date=None,
            country_code=self.country_code)
    except MultipleSymbolsFound:
        return 0
    except SymbolNotFound:
        return numpy.nan