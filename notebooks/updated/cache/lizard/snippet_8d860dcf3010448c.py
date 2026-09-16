def add_res(acc, elem):
    if not isinstance(elem, list):
        elem = [elem]
    if acc is None:
        acc = []
    for x in elem:
        acc.append(x)
    return acc