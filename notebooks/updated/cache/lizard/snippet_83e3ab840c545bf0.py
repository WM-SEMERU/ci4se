def _read_ftdna_famfinder(file):
    df = pd.read_csv(file, comment='#', na_values='-', names=['rsid',
        'chrom', 'pos', 'allele1', 'allele2'], index_col=0, dtype={'chrom':
        object})
    df['genotype'] = df['allele1'] + df['allele2']
    del df['allele1']
    del df['allele2']
    return sort_snps(df), 'FTDNA'