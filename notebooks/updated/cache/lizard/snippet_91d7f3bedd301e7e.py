def search(reader, key, prev_size=0, compare_func=cmp, block_size=8192):
    iter_ = binsearch(reader, key, compare_func, block_size)
    iter_ = linearsearch(iter_, key, prev_size=prev_size, compare_func=
        compare_func)
    return iter_