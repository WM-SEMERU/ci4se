def get_module(self):
    for md in SUPPORTED_MODULES:
        maybe_module = self.get_child_by_name(md)
        if maybe_module:
            return maybe_module
    return None