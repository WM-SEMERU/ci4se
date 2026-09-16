def percentile_ranks(self, affinities, allele=None, alleles=None, throw=True):
    if allele is not None:
        try:
            transform = self.allele_to_percent_rank_transform[allele]
            return transform.transform(affinities)
        except KeyError:
            msg = 'Allele %s has no percentile rank information' % allele
            if throw:
                raise ValueError(msg)
            else:
                warnings.warn(msg)
                return numpy.ones(len(affinities)) * numpy.nan
    if alleles is None:
        raise ValueError('Specify allele or alleles')
    df = pandas.DataFrame({'affinity': affinities})
    df['allele'] = alleles
    df['result'] = numpy.nan
    for allele, sub_df in df.groupby('allele'):
        df.loc[sub_df.index, 'result'] = self.percentile_ranks(sub_df.
            affinity, allele=allele, throw=throw)
    return df.result.values