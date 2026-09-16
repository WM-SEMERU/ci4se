def genotype_to_df(g, samples, as_string=False):
    name = g.variant.name if g.variant.name else 'genotypes'
    df = pd.DataFrame(g.genotypes, index=samples, columns=[name])
    if as_string:
        df['alleles'] = None
        hard_calls = df[name].round()
        df.loc[hard_calls == 0, 'alleles'] = '{0}/{0}'.format(g.reference)
        df.loc[hard_calls == 1, 'alleles'] = '{0}/{1}'.format(g.reference,
            g.coded)
        df.loc[hard_calls == 2, 'alleles'] = '{0}/{0}'.format(g.coded)
        df = df[['alleles']]
        df.columns = [name]
    return df