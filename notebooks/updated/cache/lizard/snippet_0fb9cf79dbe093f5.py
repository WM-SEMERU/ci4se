def difference(b, a):
    a = set(a)
    result = []
    for item in b:
        if item not in a:
            result.append(item)
    return result