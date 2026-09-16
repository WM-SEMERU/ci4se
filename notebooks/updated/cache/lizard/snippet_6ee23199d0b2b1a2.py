def entropy(string):
    p, lns = Counter(string), float(len(string))
    return -sum(count / lns * math.log(count / lns, 2) for count in p.values())