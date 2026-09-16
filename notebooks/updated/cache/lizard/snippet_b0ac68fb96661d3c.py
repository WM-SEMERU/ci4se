def signature(self):
    sig_elems = [self.seqid, self.source, self.type, self.start, self.end,
        self.strand, self.phase]
    if re.search('exon|CDS|UTR', self.type):
        parent = self.get_attr('Parent')
        if parent:
            locus, iso = atg_name(parent, retval='locus,iso', trimpad0=False)
            if locus:
                sig_elems.append(locus)
    else:
        sig_elems.extend([self.accn])
    return ','.join(str(elem) for elem in sig_elems)