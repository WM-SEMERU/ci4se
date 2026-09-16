def datapt_to_system(self, datapt, system=None, coords='data', naxispath=None):
    if self.coordsys == 'raw':
        raise WCSError('No usable WCS')
    raise NotImplementedError