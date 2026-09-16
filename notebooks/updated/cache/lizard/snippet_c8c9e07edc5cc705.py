def get_extension(self, protocol):
    if protocol not in self.registry:
        raise NoProtocolError('No protocol for %s' % protocol)
    index = self.registry[protocol]
    return self.extensions[index]