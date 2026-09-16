def __liftover_coordinates_size_match(self, intersecting_region):
    consensus_match_length = self.consensus_end - self.consensus_start
    assert consensus_match_length - len(self) == 0
    if self.consensus_match_strand is '+':
        s = max(intersecting_region.start - self.start, 0
            ) + self.consensus_start
        e = min(max(intersecting_region.end - self.start, 0) + self.
            consensus_start, self.consensus_len)
        g = GenomicInterval(self.repeat_name(), s, e, intersecting_region.
            name, intersecting_region.score, self.strand)
        return g
    elif self.consensus_match_strand is '-':
        e = self.consensus_end - max(intersecting_region.start - self.start, 0)
        s = self.consensus_end - min(max(intersecting_region.end - self.
            start, 0), len(self))
        g = GenomicInterval(self.repeat_name(), s, e, intersecting_region.
            name, intersecting_region.score, self.strand)
        return g
    else:
        raise RetrotransposonError("couldn't determine strand of " +
            'retrotransposon occurrance ' + str(self))