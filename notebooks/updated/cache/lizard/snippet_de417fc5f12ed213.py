def iterator_mix(*iterators):
    while True:
        one_left = False
        for it in iterators:
            try:
                yield it.next()
            except StopIteration:
                pass
            else:
                one_left = True
        if not one_left:
            break