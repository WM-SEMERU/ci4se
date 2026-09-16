def _create_node(self, name, factory, directory=None, create=1):
    import SCons.Util
    node = factory(name, directory, create)
    node.set_noclean(self.noclean)
    node.set_precious(self.precious)
    if self.nodefault:
        self.env.Ignore('.', node)
    if self.alias:
        self.env.AlwaysBuild(self.env.Alias(self.alias, node))
    return node