def replace_component(self, name, callable, provides=None, depends=None):
    self.remove_component(name)
    self.add_component(name, callable, provides, depends)