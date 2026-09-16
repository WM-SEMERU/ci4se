def symbol_bollinger(symbol='GOOG', start=datetime.datetime(2008, 1, 1),
    end=datetime.datetime(2009, 12, 31), price_type='close', cleaner=
    clean_dataframe, window=20, sigma=1.0):
    symbols = normalize_symbols(symbol)
    prices = price_dataframe(symbols, start=start, end=end, price_type=
        price_type, cleaner=cleaner)
    return series_bollinger(prices[symbols[0]], window=window, sigma=sigma,
        plot=False)