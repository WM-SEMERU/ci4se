def plotER(self, *args, **kwargs):
    if kwargs.pop('normed', False):
        kwargs['d2'] = 'ERnorm'
    else:
        kwargs['d2'] = 'ER'
    return self.plot(*args, **kwargs)