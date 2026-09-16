def wait_for_reactor(self, function):
    warnings.warn('@wait_for_reactor is deprecated, use @wait_for instead',
        DeprecationWarning, stacklevel=2)
    return self.wait_for(2 ** 31)(function)