def register_module(self, module, namespace=None):
    namespace = namespace if namespace is not None else module if isinstance(
        module, str) else module.__name__
    self.register_namespace(namespace, module)