def inspect_build(self, module, modname=None, path=None):
    self._module = module
    if modname is None:
        modname = module.__name__
    try:
        node = build_module(modname, module.__doc__)
    except AttributeError:
        node = build_module(modname)
    node.file = node.path = os.path.abspath(path) if path else path
    node.name = modname
    MANAGER.cache_module(node)
    node.package = hasattr(module, '__path__')
    self._done = {}
    self.object_build(node, module)
    return node