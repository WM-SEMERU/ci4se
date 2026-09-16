def _make_blocks(records):
    sparse_blocks = []
    total = len(records)
    if total == 0:
        return []
    x = 0
    while x < total:
        recstart = records[x]
        y = x
        recnum = recstart
        while y + 1 < total:
            y = y + 1
            nextnum = records[y]
            diff = nextnum - recnum
            if diff == 1:
                recnum = nextnum
            else:
                y = y - 1
                break
        ablock = []
        ablock.append(recstart)
        if y + 1 == total:
            recend = records[total - 1]
        else:
            recend = records[y]
        x = y + 1
        ablock.append(recend)
        sparse_blocks.append(ablock)
    return sparse_blocks