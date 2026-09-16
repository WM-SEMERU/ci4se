def count(start=0, step=1, *, interval=0):
    agen = from_iterable.raw(itertools.count(start, step))
    return time.spaceout.raw(agen, interval) if interval else agen