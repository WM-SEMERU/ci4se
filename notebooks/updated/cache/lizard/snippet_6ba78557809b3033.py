def child_set(self, child, **kwargs):
    for name, value in kwargs.items():
        name = name.replace('_', '-')
        self.child_set_property(child, name, value)