def get(self, name):
    if name.startswith('#'):
        return self.tags.get(name[1:])
    return self.props.get(name)