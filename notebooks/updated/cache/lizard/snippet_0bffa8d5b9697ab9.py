def find_all(self, name=None, **attrs):
    r
    for descendant in self.__descendants():
        if hasattr(descendant, '__match__') and descendant.__match__(name,
            attrs):
            yield descendant