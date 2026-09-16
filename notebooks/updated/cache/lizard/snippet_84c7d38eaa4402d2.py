def list_more(fn, offset, size, batch_size, *args):
    if size < 0:
        expected_total_size = six.MAXSIZE
    else:
        expected_total_size = size
        batch_size = min(size, batch_size)
    response = None
    total_count_got = 0
    while True:
        ret = fn(*args, offset=offset, size=batch_size)
        if response is None:
            response = ret
        else:
            response.merge(ret)
        count = ret.get_count()
        total = ret.get_total()
        offset += count
        total_count_got += count
        batch_size = min(batch_size, expected_total_size - total_count_got)
        if (count == 0 or offset >= total or total_count_got >=
            expected_total_size):
            break
    return response