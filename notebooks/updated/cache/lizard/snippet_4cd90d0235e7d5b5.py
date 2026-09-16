def update(self, values):
    for k, v in values.items():
        root, sub = self.split(k)
        if sub is None:
            self.declarations[root] = v
        else:
            self.contexts[root][sub] = v
    extra_context_keys = set(self.contexts) - set(self.declarations)
    if extra_context_keys:
        raise errors.InvalidDeclarationError(
            'Received deep context for unknown fields: %r (known=%r)' % ({
            self.join(root, sub): v for root in extra_context_keys for sub,
            v in self.contexts[root].items()}, sorted(self.declarations)))