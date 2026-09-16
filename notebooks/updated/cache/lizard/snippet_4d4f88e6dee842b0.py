def lookup_symbols(self, symbols, as_of_date, fuzzy=False, country_code=None):
    if not symbols:
        return []
    multi_country = country_code is None
    if fuzzy:
        f = self._lookup_symbol_fuzzy
        mapping = self._choose_fuzzy_symbol_ownership_map(country_code)
    else:
        f = self._lookup_symbol_strict
        mapping = self._choose_symbol_ownership_map(country_code)
    if mapping is None:
        raise SymbolNotFound(symbol=symbols[0])
    memo = {}
    out = []
    append_output = out.append
    for sym in symbols:
        if sym in memo:
            append_output(memo[sym])
        else:
            equity = memo[sym] = f(mapping, multi_country, sym, as_of_date)
            append_output(equity)
    return out