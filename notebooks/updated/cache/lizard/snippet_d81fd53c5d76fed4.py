def findrec(s, data):
    datablock = []
    for rec in data:
        if s == rec[0]:
            datablock.append([rec[1], rec[2], rec[3], rec[4]])
    return datablock