def Fisher(d1, d2, tag=None):
    assert int(d1
        ) == d1 and d1 >= 1, 'Fisher (F) "d1" must be an integer greater than 0'
    assert int(d2
        ) == d2 and d2 >= 1, 'Fisher (F) "d2" must be an integer greater than 0'
    return uv(ss.f(d1, d2), tag=tag)