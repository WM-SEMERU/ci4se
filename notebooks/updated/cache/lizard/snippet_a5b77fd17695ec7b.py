def sitespeptidesproteins(df, site_localization_probability=0.75):
    sites = filters.filter_localization_probability(df,
        site_localization_probability)['Sequence window']
    peptides = set(df['Sequence window'])
    proteins = set([str(p).split(';')[0] for p in df['Proteins']])
    return len(sites), len(peptides), len(proteins)