def histogram(data):
    ret = {}
    for datum in data:
        if datum in ret:
            ret[datum] += 1
        else:
            ret[datum] = 1
    return ret