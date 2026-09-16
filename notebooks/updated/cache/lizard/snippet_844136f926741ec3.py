def binsearch_offset(reader, key, compare_func=cmp, block_size=8192):
    min_ = 0
    reader.seek(0, 2)
    max_ = int(reader.tell() / block_size)
    while max_ - min_ > 1:
        mid = int(min_ + (max_ - min_) / 2)
        reader.seek(mid * block_size)
        if mid > 0:
            reader.readline()
        line = reader.readline()
        if compare_func(key, line) > 0:
            min_ = mid
        else:
            max_ = mid
    return min_ * block_size