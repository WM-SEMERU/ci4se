def get_method(self, name):
    if name in self.method_map:
        return self.method_map[name]
    for prefix, subdispatchers in self.subdispatchers.items():
        if name.startswith(prefix):
            for sd in subdispatchers:
                try:
                    return sd.get_method(name[len(prefix):])
                except exc.MethodNotFoundError:
                    pass
    raise exc.MethodNotFoundError(name)