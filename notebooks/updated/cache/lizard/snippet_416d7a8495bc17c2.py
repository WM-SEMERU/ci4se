def filter(self, fn, skip_na=True, seed=None):
    assert callable(fn), 'Input must be callable'
    if seed is None:
        seed = abs(hash('%0.20f' % time.time())) % 2 ** 31
    with cython_context():
        return SArray(_proxy=self.__proxy__.filter(fn, skip_na, seed))