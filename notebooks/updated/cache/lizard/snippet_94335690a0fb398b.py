def left(self, num=None):
    if num == None:
        return FlatList([_get_list(self)[0]])
    if num <= 0:
        return Null
    return FlatList(_get_list(self)[:num])