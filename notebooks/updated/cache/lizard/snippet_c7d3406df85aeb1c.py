def drift(data, n=3, **kwargs):
    yi = data[-n]
    yf = data[-1]
    slope = (yf - yi) / (n - 1)
    forecast = yf + slope
    return forecast