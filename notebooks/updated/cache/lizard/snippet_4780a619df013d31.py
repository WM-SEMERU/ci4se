def get_market_book(symbols=None, **kwargs):
    import warnings
    warnings.warn(WNG_MSG % ('get_market_book', 'iexdata.get_deep_book'))
    return Book(symbols, **kwargs).fetch()