def clone(self):
    obj = self.__class__()
    obj.libs = deepcopy(self.libs)
    return obj