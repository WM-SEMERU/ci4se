def count_the_same(iterable, sentinel):
    count = 0
    x = None
    for count, x in enumerate(iterable):
        if x != sentinel:
            break
    return count, x