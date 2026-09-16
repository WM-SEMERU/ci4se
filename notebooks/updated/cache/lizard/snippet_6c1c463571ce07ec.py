def nonuniq(iterable):
    temp_dict = {}
    for e in iterable:
        if e in temp_dict:
            yield e
        temp_dict.setdefault(e, e)