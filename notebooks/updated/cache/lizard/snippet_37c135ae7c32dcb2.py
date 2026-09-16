def get_string_module(self, code, resource=None, force_errors=False):
    return PyModule(self, code, resource, force_errors=force_errors)