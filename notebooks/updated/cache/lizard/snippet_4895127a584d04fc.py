def _generate_lags(maxlag, multiplier):
    r
    lags = [1]
    lag = 1.0
    import decimal
    while lag <= maxlag:
        lag = lag * multiplier
        lag = int(decimal.Decimal(lag).quantize(decimal.Decimal('1'),
            rounding=decimal.ROUND_HALF_UP))
        if lag <= maxlag:
            ilag = int(lag)
            lags.append(ilag)
    if maxlag not in lags:
        lags.append(maxlag)
    return np.array(lags)