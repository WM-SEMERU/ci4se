def query_locus(self, filter_column, filter_value, feature):
    loci = self.query_loci(filter_column=filter_column, filter_value=
        filter_value, feature=feature)
    if len(loci) == 0:
        raise ValueError("Couldn't find locus for %s with %s = %s" % (
            feature, filter_column, filter_value))
    elif len(loci) > 1:
        raise ValueError('Too many loci for %s with %s = %s: %s' % (feature,
            filter_column, filter_value, loci))
    return loci[0]