def new_action(self, method='GET', **kwargs):
    if method not in self.methods:
        raise TypeError('{} not in valid method(s): {}.'.format(method,
            self.methods))
    return Action(self, method, **kwargs)