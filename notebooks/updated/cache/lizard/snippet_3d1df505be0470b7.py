def prokka_table(self):
    headers = OrderedDict()
    headers['organism'] = {'title': 'Organism', 'description': 'Organism name'}
    headers['contigs'] = {'title': '# contigs', 'description':
        'Number of contigs in assembly', 'format': '{:i}'}
    headers['bases'] = {'title': '# bases', 'description':
        'Number of nucleotide bases in assembly', 'format': '{:i}'}
    headers['CDS'] = {'title': '# CDS', 'description':
        'Number of annotated CDS', 'format': '{:i}'}
    headers['rRNA'] = {'title': '# rRNA', 'description':
        'Number of annotated rRNA', 'format': '{:i}'}
    headers['tRNA'] = {'title': '# tRNA', 'description':
        'Number of annotated tRNA', 'format': '{:i}'}
    headers['tmRNA'] = {'title': '# tmRNA', 'description':
        'Number of annotated tmRNA', 'format': '{:i}'}
    headers['misc_RNA'] = {'title': '# misc RNA', 'description':
        'Number of annotated misc. RNA', 'format': '{:i}'}
    headers['sig_peptide'] = {'title': '# sig_peptide', 'description':
        'Number of annotated sig_peptide', 'format': '{:i}'}
    headers['repeat_region'] = {'title': '# CRISPR arrays', 'description':
        'Number of annotated CRSIPR arrays', 'format': '{:i}'}
    table_config = {'namespace': 'prokka', 'min': 0}
    return table.plot(self.prokka, headers, table_config)