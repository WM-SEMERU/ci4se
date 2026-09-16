def create_index(self, name, recreate=False, _type='default'):
    if name not in self.indexes or recreate:
        self.build_index(name, _type)