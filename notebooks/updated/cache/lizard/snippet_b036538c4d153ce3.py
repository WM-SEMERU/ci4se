def binarySearchPos(seq, item, cmpfunc=cmp):
    r
    if not seq:
        return -1
    left, right = 0, len(seq) - 1
    if cmpfunc(seq[left], item) == 1 and cmpfunc(seq[right], item) == -1:
        return -1
    while left <= right:
        halfPoint = (left + right) // 2
        comp = cmpfunc(seq[halfPoint], item)
        if comp > 0:
            right = halfPoint - 1
        elif comp < 0:
            left = halfPoint + 1
        else:
            return halfPoint
    return -1