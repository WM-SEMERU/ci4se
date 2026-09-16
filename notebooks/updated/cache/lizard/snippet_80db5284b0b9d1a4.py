def list_all_elements(self):
    res = []
    if self.operand in ['host', 'service']:
        return [self.sons[0]]
    for son in self.sons:
        res.extend(son.list_all_elements())
    return list(set(res))