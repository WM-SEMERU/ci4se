def macd(series, fast=3, slow=10, smooth=16):
    macd_line = rolling_weighted_mean(series, window=fast
        ) - rolling_weighted_mean(series, window=slow)
    signal = rolling_weighted_mean(macd_line, window=smooth)
    histogram = macd_line - signal
    return pd.DataFrame(index=series.index, data={'macd': macd_line.values,
        'signal': signal.values, 'histogram': histogram.values})