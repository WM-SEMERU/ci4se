def get_size_str(size):
    if size == 0:
        magnitude = 0
        level = 0
    else:
        magnitude = math.floor(math.log(size, 10))
        level = int(min(math.floor(magnitude // 3), 4))
    return ('%d' if level == 0 else '%.2f') % (float(size) / 2 ** (level * 10)
        ) + ' ' + SIZE_LEVEL[level]