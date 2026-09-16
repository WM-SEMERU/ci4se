def split_limits_heads(self):
    heads = []
    new_limit_to = []
    for limit in self.limit_to:
        if '.' in limit:
            name, limit = limit.split('.', 1)
            heads.append(name)
            new_limit_to.append(limit)
        else:
            heads.append(limit)
    return heads, new_limit_to