def Target_setAttachToFrames(self, value):
    assert isinstance(value, (bool,)
        ), "Argument 'value' must be of type '['bool']'. Received type: '%s'" % type(
        value)
    subdom_funcs = self.synchronous_command('Target.setAttachToFrames',
        value=value)
    return subdom_funcs