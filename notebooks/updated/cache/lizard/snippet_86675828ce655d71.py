def factory(self, classname, *args, **kwargs):
    klass = self.load_class(classname)
    return self.get_factory_by_class(klass)(*args, **kwargs)