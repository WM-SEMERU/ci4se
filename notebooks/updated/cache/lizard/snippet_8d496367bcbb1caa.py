def remove_child(self, index):
    if index < 0 or index > len(self.__children):
        return
    child = self.__children.pop(index)
    child.parent = None
    return child