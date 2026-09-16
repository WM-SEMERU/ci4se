def compounding(start, stop, compound, t=0.0):
    curr = float(start)
    while True:
        yield _clip(curr, start, stop)
        curr *= compound