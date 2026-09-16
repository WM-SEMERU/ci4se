def every_other(pipe, how_many=1):
    for i, x in zip(pipe, cycle(repeater([True, False], how_many))):
        if x:
            yield i