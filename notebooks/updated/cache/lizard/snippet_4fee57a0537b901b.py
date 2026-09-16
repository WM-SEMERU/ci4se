def DOM_pushNodeByPathToFrontend(self, path):
    assert isinstance(path, (str,)
        ), "Argument 'path' must be of type '['str']'. Received type: '%s'" % type(
        path)
    subdom_funcs = self.synchronous_command('DOM.pushNodeByPathToFrontend',
        path=path)
    return subdom_funcs