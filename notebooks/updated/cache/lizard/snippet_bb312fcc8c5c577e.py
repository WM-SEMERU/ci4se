def _clear(self, title=True, xlabel=True, ylabel=True):
    if title:
        pyl.title('')
    if xlabel:
        pyl.xlabel('')
    if ylabel:
        pyl.ylabel('')