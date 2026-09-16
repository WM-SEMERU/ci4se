def n_to_g(self, n_interval):
    frs, fre = n_interval.start.base - 1, n_interval.end.base - 1
    start_offset, end_offset = n_interval.start.offset, n_interval.end.offset
    if self.strand == -1:
        fre, frs = self.tgt_len - frs - 1, self.tgt_len - fre - 1
        start_offset, end_offset = -end_offset, -start_offset
    grs, _, grs_cigar = self._map(from_pos=self.tgt_pos, to_pos=self.
        ref_pos, pos=frs, base='start')
    gre, _, gre_cigar = self._map(from_pos=self.tgt_pos, to_pos=self.
        ref_pos, pos=fre, base='end')
    grs, gre = grs + self.gc_offset + 1, gre + self.gc_offset + 1
    gs, ge = grs + start_offset, gre + end_offset
    return hgvs.location.Interval(start=hgvs.location.SimplePosition(gs,
        uncertain=n_interval.start.uncertain), end=hgvs.location.
        SimplePosition(ge, uncertain=n_interval.end.uncertain), uncertain=
        grs_cigar in 'DI' or gre_cigar in 'DI')