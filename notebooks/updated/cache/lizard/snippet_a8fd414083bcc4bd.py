def centralize(data, time=False, units=False):
    assert time is not False or units is not False
    res = copy.copy(data)
    if time is True:
        res = np.array([(x - np.mean(x)) for x in res])
    if units is True:
        res = np.array(res - np.mean(res, axis=0))
    return res