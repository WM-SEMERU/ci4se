def sizes(x):

    def size(x):
        try:
            return x.size
        except Exception:
            return 0
    return nested_map(x, size)