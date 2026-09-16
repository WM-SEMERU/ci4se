def get(self, node, path):
    node, parts = self.__start(node, path)
    for part in parts:
        if part == '..':
            node = node.parent
        elif part in ('', '.'):
            pass
        else:
            node = self.__get(node, part)
    return node