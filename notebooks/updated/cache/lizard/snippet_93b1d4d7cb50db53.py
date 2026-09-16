def repvals(self, method):
    if method == 'pct':
        return pk_scoreatpercentile(self.d, [50.0, 84.134, 15.866])
    if method == 'gauss':
        m, s = self.d.mean(), self.d.std()
        return np.asarray([m, m + s, m - s])
    raise ValueError('unknown representative-value method "%s"' % method)