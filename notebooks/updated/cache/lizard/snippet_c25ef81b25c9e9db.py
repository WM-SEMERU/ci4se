def walk(self, filters: str=None, filter_type: type=None, pprint=False,
    depth=-1):
    children = self.children()
    if children is None:
        children = []
    res = []
    if depth == 0:
        return res
    elif depth != -1:
        depth -= 1
    for child in children:
        if isinstance(child, Formula):
            tmp = child.walk(filters=filters, filter_type=filter_type,
                pprint=pprint, depth=depth)
            if tmp:
                res.extend(tmp)
    if filter_type is None:
        if filters is not None:
            if eval(filters) is True:
                res.append(self)
        else:
            res.append(self)
    elif isinstance(self, filter_type):
        if filters is not None:
            if eval(filters) is True:
                res.append(self)
        else:
            res.append(self)
    if pprint:
        res = [(str(x) + ' ') for x in res]
        res = '\n'.join(res)
    return res