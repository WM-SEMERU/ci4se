def create_groups(self, *names, **kwargs):
    return tuple(self.create_group(name, **kwargs) for name in names)