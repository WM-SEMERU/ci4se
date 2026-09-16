def remove_all(gset, elem):
    n = 0
    while True:
        try:
            remove_once(gset, elem)
            n = n + 1
        except RemoveError:
            return n