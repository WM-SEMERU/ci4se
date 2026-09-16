def mi(x, y):
    try:
        if isinstance(x, zip):
            x = list(x)
        if isinstance(y, zip):
            y = list(y)
    except:
        pass
    probX = symbols_to_prob(x).prob()
    probY = symbols_to_prob(y).prob()
    probXY = symbols_to_prob(combine_symbols(x, y)).prob()
    return entropy(prob=probX) + entropy(prob=probY) - entropy(prob=probXY)