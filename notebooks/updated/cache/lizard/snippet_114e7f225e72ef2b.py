def letter2num(letters, zbase=False):
    letters = letters.upper()
    res = 0
    weight = len(letters) - 1
    assert weight >= 0, letters
    for i, c in enumerate(letters):
        assert 65 <= ord(c) <= 90, c
        res += (ord(c) - 64) * 26 ** (weight - i)
    if not zbase:
        return res
    return res - 1