def scope_lookup(self, node, name, offset=0):
    if name in self.scope_attrs and name not in self.locals:
        try:
            return self, self.getattr(name)
        except exceptions.AttributeInferenceError:
            return self, ()
    return self._scope_lookup(node, name, offset)