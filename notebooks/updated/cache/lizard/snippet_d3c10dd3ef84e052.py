def sort_snps(snps):
    sorted_list = sorted(snps['chrom'].unique(), key=_natural_sort_key)
    if 'PAR' in sorted_list:
        sorted_list.remove('PAR')
        sorted_list.append('PAR')
    if 'MT' in sorted_list:
        sorted_list.remove('MT')
        sorted_list.append('MT')
    snps['chrom'] = snps['chrom'].astype(CategoricalDtype(categories=
        sorted_list, ordered=True))
    snps = snps.sort_values(['chrom', 'pos'])
    snps['chrom'] = snps['chrom'].astype(object)
    return snps