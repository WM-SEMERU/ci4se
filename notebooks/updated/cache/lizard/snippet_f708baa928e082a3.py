def parse_tstv_summary(self):
    self.vcftools_tstv_summary = dict()
    for f in self.find_log_files('vcftools/tstv_summary', filehandles=True):
        d = {}
        for line in f['f'].readlines()[1:]:
            key = line.split()[0]
            val = int(line.split()[1])
            d[key] = val
        self.vcftools_tstv_summary[f['s_name']] = d
    self.vcftools_tstv_summary = self.ignore_samples(self.vcftools_tstv_summary
        )
    if len(self.vcftools_tstv_summary) == 0:
        return 0
    keys = OrderedDict()
    keys = ['AC', 'AG', 'AT', 'CG', 'CT', 'GT', 'Ts', 'Tv']
    pconfig = {'id': 'vcftools_tstv_summary', 'title':
        'VCFTools: TsTv Summary', 'ylab': 'Counts'}
    self.add_section(name='TsTv Summary', anchor='vcftools-tstv-summary',
        description=
        'Plot of `TSTV-SUMMARY` - count of different types of transition and transversion SNPs.'
        , plot=bargraph.plot(self.vcftools_tstv_summary, keys, pconfig))
    return len(self.vcftools_tstv_summary)