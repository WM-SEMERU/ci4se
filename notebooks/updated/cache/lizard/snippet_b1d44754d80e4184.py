def mro(self, cls):
    ups = inspect.getmro(cls.cls)
    return list(map(lambda c: self.find_class(c), ups))