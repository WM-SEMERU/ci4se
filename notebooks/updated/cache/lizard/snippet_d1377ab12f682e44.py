def rpc_get_names(self, filename, source, offset):
    source = get_source(source)
    if hasattr(self.backend, 'rpc_get_names'):
        return self.backend.rpc_get_names(filename, source, offset)
    else:
        raise Fault('get_names not implemented by current backend', code=400)