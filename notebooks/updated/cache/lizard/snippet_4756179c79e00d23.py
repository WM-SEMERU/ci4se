def _read_ancestry(file):
    df = pd.read_csv(file, comment='#', header=0, sep='\t', na_values=0,
        names=['rsid', 'chrom', 'pos', 'allele1', 'allele2'], index_col=0,
        dtype={'chrom': object})
    df['genotype'] = df['allele1'] + df['allele2']
    del df['allele1']
    del df['allele2']
    df.ix[np.where(df['chrom'] == '23')[0], 'chrom'] = 'X'
    df.ix[np.where(df['chrom'] == '24')[0], 'chrom'] = 'Y'
    df.ix[np.where(df['chrom'] == '25')[0], 'chrom'] = 'PAR'
    df.ix[np.where(df['chrom'] == '26')[0], 'chrom'] = 'MT'
    return sort_snps(df), 'AncestryDNA'