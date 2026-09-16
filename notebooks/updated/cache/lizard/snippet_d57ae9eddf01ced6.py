def diff_iter(self, other, **kwargs):
    for diff in super(JsonRecord, self).diff_iter(other, **kwargs):
        newargs = diff.__getstate__()
        yield JsonDiffInfo(**newargs)