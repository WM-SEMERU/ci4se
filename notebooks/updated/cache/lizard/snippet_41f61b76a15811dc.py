def runs_per_second(generator, seconds=3):
    assert isinstance(seconds, int
        ), 'runs_per_second needs seconds to be an int, not {}'.format(repr
        (seconds))
    assert seconds > 0, 'runs_per_second needs seconds to be positive, not {}'.format(
        repr(seconds))
    if callable(generator) and not any(i in ('next', '__next__', '__iter__'
        ) for i in dir(generator)):
        try:
            output = generator()
        except:
            raise Exception(
                'runs_per_second needs a working function that accepts no arguments'
                )
        else:
            generator = iter(generator, 1 if output is None else None)
            del output
    c = 0
    entire_test_time_used = False
    start = ts()
    end = start + seconds
    for _ in generator:
        if ts() > end:
            entire_test_time_used = True
            break
        else:
            c += 1
    duration = ts() - start
    return int(c / (seconds if entire_test_time_used else duration))