def childAtPath(self, path):
    if self.__root is None:
        return None
    if path[0] == '/':
        path = path[1:]
    path = path.split('/', 1)
    if self.getChild(path[0]) is None:
        return None
    if len(path) > 1:
        return self.__root.childAtPath(path[1])
    else:
        return self.__root