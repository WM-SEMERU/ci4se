def iqr(b, perc=(25, 75)):
    b = checkma(b)
    low, high = calcperc(b, perc)
    return low, high, high - low