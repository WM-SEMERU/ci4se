def copy_from(self, other_state):
    for prop in self.properties().values():
        setattr(self, prop.name, getattr(other_state, prop.name))