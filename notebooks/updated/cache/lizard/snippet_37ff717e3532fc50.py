def unweave(iterable, n=2):
    r
    res = [[] for i in range(n)]
    i = 0
    for x in iterable:
        res[i % n].append(x)
        i += 1
    return res