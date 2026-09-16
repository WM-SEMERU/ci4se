def tag_info_chart(self):
    ucsc = [('chr' + str(i)) for i in range(1, 23)].append(['chrX', 'chrY',
        'chrM'])
    ensembl = list(range(1, 23)).append(['X', 'Y', 'MT'])
    pconfig = {'id': 'tagInfo', 'title': 'Homer: Tag Info Distribution',
        'ylab': 'Tags', 'cpswitch_counts_label': 'Number of Tags'}
    sample1 = next(iter(self.tagdir_data['taginfo_total']))
    chrFormat = next(iter(self.tagdir_data['taginfo_total'][sample1]))
    if 'chr' in chrFormat:
        chrs = ucsc
    else:
        chrs = ensembl
    return bargraph.plot(self.tagdir_data['taginfo_total'], chrs, pconfig)