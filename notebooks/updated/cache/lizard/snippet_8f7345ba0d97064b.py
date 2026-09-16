def CSS_setStyleTexts(self, edits):
    assert isinstance(edits, (list, tuple)
        ), "Argument 'edits' must be of type '['list', 'tuple']'. Received type: '%s'" % type(
        edits)
    subdom_funcs = self.synchronous_command('CSS.setStyleTexts', edits=edits)
    return subdom_funcs