def features(self, ignore_unknown=False):
    if not self.db:
        raise ValueError('Please attach a gffutils.FeatureDB')
    for i in self.data.index:
        try:
            yield gffutils.helpers.asinterval(self.db[i])
        except gffutils.FeatureNotFoundError:
            if ignore_unknown:
                continue
            else:
                raise gffutils.FeatureNotFoundError('%s not found' % i)