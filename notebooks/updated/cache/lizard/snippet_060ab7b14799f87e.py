def piGenGosper():
    z = (1, 0, 0, 1), 1
    while True:
        lft = __lfts(z[1])
        n = int(__next(z))
        if __safe(z, n):
            z = __prod(z, n)
            yield n
        else:
            z = __cons(z, lft)