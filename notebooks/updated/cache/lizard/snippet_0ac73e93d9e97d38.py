def sample(self, fraction, seed=None, exact=False):
    if seed is None:
        seed = abs(hash('%0.20f' % time.time())) % 2 ** 31
    if fraction > 1 or fraction < 0:
        raise ValueError('Invalid sampling rate: ' + str(fraction))
    if self.num_rows() == 0 or self.num_columns() == 0:
        return self
    else:
        with cython_context():
            return SFrame(_proxy=self.__proxy__.sample(fraction, seed, exact))