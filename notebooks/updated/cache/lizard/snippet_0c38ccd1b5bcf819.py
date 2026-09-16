def lazy_property_factory(lazy_property):

    def lazy_property_getter(self):
        if not hasattr(self, '_' + lazy_property):
            self.load()
        if not hasattr(self, '_' + lazy_property):
            raise ValueError("{} wasn't loaded".format(lazy_property))
        return getattr(self, '_' + lazy_property)

    def lazy_property_setter(self, value):
        setattr(self, '_' + lazy_property, value)
    return lazy_property_getter, lazy_property_setter