def dedupe_list(l):
    result = []
    for el in l:
        if el not in result:
            result.append(el)
    return result