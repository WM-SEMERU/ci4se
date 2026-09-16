def are_stringable_keys(self, m):
    for x in m.keys():
        if len(self.handlers[x].tag(x)) != 1:
            return False
    return True