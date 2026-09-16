def get_nts(self, fin_davidchart):
    nts = []
    with open(fin_davidchart) as ifstrm:
        hdr_seen = False
        for line in ifstrm:
            line = line.rstrip()
            flds = line.split('\t')
            if hdr_seen:
                ntd = self._init_nt(flds)
                nts.append(ntd)
            elif line[:8] == 'Category':
                assert len(flds) == 13, len(flds)
                hdr_seen = True
        sys.stdout.write('  READ {N:5} GO IDs from DAVID Chart: {TSV}\n'.
            format(N=len(nts), TSV=fin_davidchart))
    return nts