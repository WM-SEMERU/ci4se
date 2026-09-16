def search_greater(values, target):
    first = 0
    last = len(values)
    while first < last:
        middle = (first + last) // 2
        if values[middle][0] < target:
            first = middle + 1
        else:
            last = middle
    return first