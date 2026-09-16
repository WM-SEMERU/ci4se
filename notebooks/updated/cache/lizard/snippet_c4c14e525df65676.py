def line(loc, strg):
    lastCR = strg.rfind('\n', 0, loc)
    nextCR = strg.find('\n', loc)
    if nextCR >= 0:
        return strg[lastCR + 1:nextCR]
    else:
        return strg[lastCR + 1:]