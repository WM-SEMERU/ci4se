def pair_looper(iterator):
    left = START
    for item in iterator:
        if left is not START:
            yield left, item
        left = item