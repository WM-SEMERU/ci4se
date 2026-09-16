def iprotate(l, steps=1):
    r
    if len(l):
        steps %= len(l)
        if steps:
            firstPart = l[:steps]
            del l[:steps]
            l.extend(firstPart)
    return l