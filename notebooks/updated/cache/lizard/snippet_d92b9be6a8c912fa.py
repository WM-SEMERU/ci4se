def append(cls, d, s, filter=Filter()):
    for item in s:
        if item in filter:
            d.append(item)