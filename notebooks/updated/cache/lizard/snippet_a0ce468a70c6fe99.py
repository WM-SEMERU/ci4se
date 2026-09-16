def data(path, hours, offset=0):
    now = time.time()
    end = now - _to_sec(offset)
    start = end - _to_sec(hours)
    _data = whisper.fetch(path, start, end)
    return all(x is None for x in _data[-1])