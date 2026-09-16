def ReportConfiguration(self, file):
    global encodingpar
    print >> file, libgwas.BuildReportLine('MACH_ARCHIVES', '')
    if self.chrpos_encoding:
        print >> file, libgwas.BuildReportLine('MACH_CHRPOS', 
            'IDS expected to be in format chr:pos' +
            ' SNP boundary filters might not work ' +
            '(see manual for details)')
    else:
        print >> file, libgwas.BuildReportLine('MACH_CHRPOS',
            'IDs are treated like RSIDs')
    idx = 0
    for arch in self.archives[0:]:
        print >> file, libgwas.BuildReportLine('', '%s:%s' % (self.archives
            [idx], self.info_files[idx]))
        idx += 1
    print >> file, libgwas.BuildReportLine('ENCODING', ['Dosage',
        'Genotype'][encoding])